from torch.utils.tensorboard import SummaryWriter
import time
import torch
import numpy as np
from metrics import NDCGatK_r
'''
Train
'''
########################### TRAINING #####################################
def train(model, optimizer, train_loader, test_loader, mask, test_ground_truth_list, interacted_items, params): 

    
    device = params['device']
    best_epoch, best_recall, best_ndcg = 0, 0, 0
    early_stop_count = 0
    early_stop = False

    batches = len(train_loader.dataset) // params['batch_size']
    if len(train_loader.dataset) % params['batch_size'] != 0:
        batches += 1
    print('Total training batches = {}'.format(batches))
    
    if params['enable_tensorboard']:
        writer = SummaryWriter(log_dir="./writer")
    

    for epoch in range(params['max_epoch']):
        model.train() 
        start_time = time.time()

        for batch, x in enumerate(train_loader): # x: tensor:[users, pos_items]
            users, pos_items, neg_items = Sampling(x, params['item_num'], params['negative_num'], interacted_items, params['sampling_sift_pos'])
            users = users.to(device)
            pos_items = pos_items.to(device)
            neg_items = neg_items.to(device)

            model.zero_grad()
            loss = model(users, pos_items, neg_items)
            if params['enable_tensorboard']:
                writer.add_scalar("Loss/train_batch", loss, batches * epoch + batch)
            loss.backward()
            optimizer.step()
        
        train_time = time.strftime("%H: %M: %S", time.gmtime(time.time() - start_time))
        if params['enable_tensorboard']:
            writer.add_scalar("Loss/train_epoch", loss, epoch)

        need_test = True
        if epoch < 50 and epoch % 5 != 0:
            need_test = False
            
        if need_test:
            start_time = time.time()
            F1_score, Precision, Recall, NDCG = test(model, test_loader, test_ground_truth_list, mask, params['topk'], params['user_num'])
            if params['enable_tensorboard']:
                writer.add_scalar('Results/recall@20', Recall, epoch)
                writer.add_scalar('Results/ndcg@20', NDCG, epoch)
            test_time = time.strftime("%H: %M: %S", time.gmtime(time.time() - start_time))
            
            print('The time for epoch {} is: train time = {}, test time = {}'.format(epoch, train_time, test_time))
            print("Loss = {:.5f}, F1-score: {:5f} \t Precision: {:.5f}\t Recall: {:.5f}\tNDCG: {:.5f}".format(loss.item(), F1_score, Precision, Recall, NDCG))

            if Recall > best_recall:
                best_recall, best_ndcg, best_epoch = Recall, NDCG, epoch
                early_stop_count = 0
                torch.save(model.state_dict(), params['model_save_path'])

            else:
                early_stop_count += 1
                if early_stop_count == params['early_stop_epoch']:
                    early_stop = True
        
        if early_stop:
            print('##########################################')
            print('Early stop is triggered at {} epochs.'.format(epoch))
            print('Results:')
            print('best epoch = {}, best recall = {}, best ndcg = {}'.format(best_epoch, best_recall, best_ndcg))
            print('The best model is saved at {}'.format(params['model_save_path']))
            break

    writer.flush()

    print('Training end!')


def getLabel(test_data, pred_data):
    r = []
    for i in range(len(test_data)):
        groundTrue = test_data[i]
        predictTopK = pred_data[i]
        pred = list(map(lambda x: x in groundTrue, predictTopK))
        pred = np.array(pred).astype("float")
        r.append(pred)
    return np.array(r).astype('float')

def test_one_batch(X, k):
    sorted_items = X[0].numpy()
    groundTrue = X[1]
    r = getLabel(groundTrue, sorted_items)
    ret = RecallPrecision_ATk(groundTrue, r, k)
    return ret['precision'], ret['recall'], NDCGatK_r(groundTrue,r,k)


def RecallPrecision_ATk(test_data, r, k):
	"""
    test_data should be a list? cause users may have different amount of pos items. shape (test_batch, k)
    pred_data : shape (test_batch, k) NOTE: pred_data should be pre-sorted
    k : top-k
    """
	right_pred = r[:, :k].sum(1)
	precis_n = k
	
	recall_n = np.array([len(test_data[i]) for i in range(len(test_data))])
	recall_n = np.where(recall_n != 0, recall_n, 1)
	recall = np.sum(right_pred / recall_n)
	precis = np.sum(right_pred) / precis_n
	return {'recall': recall, 'precision': precis}


def test(model, test_loader, test_ground_truth_list, mask, topk, n_user):
    users_list = []
    rating_list = []
    groundTrue_list = []

    with torch.no_grad():
        model.eval()
        for idx, batch_users in enumerate(test_loader):
            
            batch_users = batch_users.to(model.get_device())
            rating = model.test_foward(batch_users) 
            rating = rating.cpu()
            rating += mask[batch_users]
            
            _, rating_K = torch.topk(rating, k=topk)
            rating_list.append(rating_K)

            groundTrue_list.append([test_ground_truth_list[u] for u in batch_users])

    X = zip(rating_list, groundTrue_list)
    Recall, Precision, NDCG = 0, 0, 0

    for i, x in enumerate(X):
        precision, recall, ndcg = test_one_batch(x, topk)
        Recall += recall
        Precision += precision
        NDCG += ndcg
        

    Precision /= n_user
    Recall /= n_user
    NDCG /= n_user
    F1_score = 2 * (Precision * Recall) / (Precision + Recall)

    return F1_score, Precision, Recall, NDCG



def Sampling(pos_train_data, item_num, neg_ratio, interacted_items, sampling_sift_pos):
	neg_candidates = np.arange(item_num)

	if sampling_sift_pos:
		neg_items = []
		for u in pos_train_data[0]:
			probs = np.ones(item_num)
			probs[interacted_items[u]] = 0
			probs /= np.sum(probs)

			u_neg_items = np.random.choice(neg_candidates, size = neg_ratio, p = probs, replace = True).reshape(1, -1)
	
			neg_items.append(u_neg_items)

		neg_items = np.concatenate(neg_items, axis = 0) 
	else:
		neg_items = np.random.choice(neg_candidates, (len(pos_train_data[0]), neg_ratio), replace = True)
	
	neg_items = torch.from_numpy(neg_items)
	
	return pos_train_data[0], pos_train_data[1], neg_items	# users, pos_items, neg_items