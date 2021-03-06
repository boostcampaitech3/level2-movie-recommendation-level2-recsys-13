## UltraGCN_Amazon_Electronics_x0

A notebook to benchmark UltraGCN on Amazon_Electronics dataset.

Author: Kelong Mao, Renmin University

Edited by [XUEPAI Team](https://github.com/xue-pai)


### Index
[Environments](#Environments) | [Dataset](#Dataset) | [Code](#Code) | [Results](#Results) | [Logs](#Logs)

### Environments
+ Hardware

    ```bash
    CPU: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.6GHz
    RAM: 128G
    ```
+ Software

    ```python
    python: 3.7.9
    pytorch 1.4.0
    numpy: 1.19.2
    scipy: 1.1.0
    tensorboard: 2.4.0
    ```

### Dataset
We follow the data split and preprocessing steps in NBPO.We directly transform the formats of the data from their [repo](https://github.com/Wenhui-Yu/NBPO).

### Code
Due to the conciseness of UltraGCN designs, we adopt the single file style to make the code clear and easy to be validated. All codes are in the file "main.py" with a configuration file "dataset_name_config.ini". The reproduction is very easy:

First, set your parameters in the file "dataset_name_config.ini". See "amazon_config.ini" for reference.


```bash
python main.py --config_file electronics_config.ini
```

### Results
F1-score@20: 0.033028 

NDCG@20 = 0.08285


### Logs
```bash
###################### UltraGCN ######################
1. Loading Configuration...
load path = ./electronics_ii_constraint_mat object
load path = ./electronics_ii_neighbor_mat object
Load Configuration OK, show them below
Configuration:
{'embedding_dim': 64, 'ii_neighbor_num': 10, 'model_save_path': './ultragcn_electronics.pt', 'max_epoch': 2000, 'enable_tensorboard': True, 'initial_weight': 0.001, 'dataset': 'electronics', 'gpu': '3', 'device': device(type='cuda', index=3), 'lr': 0.001, 'batch_size': 2048, 'early_stop_epoch': 500, 'w1': 1e-07, 'w2': 1.0, 'w3': 1e-07, 'w4': 1.0, 'negative_num': 75, 'negative_weight': 75.0, 'gamma': 5e-05, 'lambda': 1e-07, 'sampling_sift_pos': True, 'test_batch_size': 2048, 'topk': 20, 'user_num': 1435, 'item_num': 1522}
Total training batches = 16
The time for epoch 0 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 2952.26050, F1-score: 0.002596 	 Precision: 0.00146	 Recall: 0.01147	NDCG: 0.00488
The time for epoch 1 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 2580.14062, F1-score: 0.005450 	 Precision: 0.00307	 Recall: 0.02448	NDCG: 0.00985
The time for epoch 2 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 1843.62463, F1-score: 0.006221 	 Precision: 0.00352	 Recall: 0.02679	NDCG: 0.01885
The time for epoch 3 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 1188.65894, F1-score: 0.015845 	 Precision: 0.00902	 Recall: 0.06488	NDCG: 0.04004
The time for epoch 4 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 700.25769, F1-score: 0.021191 	 Precision: 0.01202	 Recall: 0.08936	NDCG: 0.04893
The time for epoch 5 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 460.13196, F1-score: 0.021529 	 Precision: 0.01223	 Recall: 0.08984	NDCG: 0.04908
The time for epoch 6 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 361.56296, F1-score: 0.021538 	 Precision: 0.01223	 Recall: 0.09015	NDCG: 0.04925
The time for epoch 7 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 313.89563, F1-score: 0.021661 	 Precision: 0.01230	 Recall: 0.09066	NDCG: 0.04944
The time for epoch 8 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 292.32629, F1-score: 0.021786 	 Precision: 0.01237	 Recall: 0.09127	NDCG: 0.04963
The time for epoch 9 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 282.00000, F1-score: 0.021788 	 Precision: 0.01237	 Recall: 0.09133	NDCG: 0.04991
The time for epoch 10 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 279.84195, F1-score: 0.021607 	 Precision: 0.01226	 Recall: 0.09067	NDCG: 0.04942
The time for epoch 11 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 273.57269, F1-score: 0.021787 	 Precision: 0.01237	 Recall: 0.09129	NDCG: 0.04989
The time for epoch 12 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 272.97046, F1-score: 0.021846 	 Precision: 0.01240	 Recall: 0.09146	NDCG: 0.04960
The time for epoch 13 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.79895, F1-score: 0.021790 	 Precision: 0.01237	 Recall: 0.09139	NDCG: 0.04983
The time for epoch 14 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.98242, F1-score: 0.021540 	 Precision: 0.01223	 Recall: 0.09021	NDCG: 0.04949
The time for epoch 15 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.19434, F1-score: 0.021666 	 Precision: 0.01230	 Recall: 0.09084	NDCG: 0.04950
The time for epoch 16 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.87061, F1-score: 0.021607 	 Precision: 0.01226	 Recall: 0.09067	NDCG: 0.04964
The time for epoch 17 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.48566, F1-score: 0.021735 	 Precision: 0.01233	 Recall: 0.09137	NDCG: 0.04983
The time for epoch 18 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.40875, F1-score: 0.021725 	 Precision: 0.01233	 Recall: 0.09102	NDCG: 0.04976
The time for epoch 19 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.88000, F1-score: 0.021417 	 Precision: 0.01216	 Recall: 0.08968	NDCG: 0.04944
The time for epoch 20 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 269.88641, F1-score: 0.021664 	 Precision: 0.01230	 Recall: 0.09077	NDCG: 0.04973
The time for epoch 21 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.79865, F1-score: 0.021475 	 Precision: 0.01220	 Recall: 0.08985	NDCG: 0.04938
The time for epoch 22 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.08414, F1-score: 0.021531 	 Precision: 0.01223	 Recall: 0.08992	NDCG: 0.04914
The time for epoch 23 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 255.99588, F1-score: 0.021787 	 Precision: 0.01237	 Recall: 0.09131	NDCG: 0.04981
The time for epoch 24 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.10135, F1-score: 0.021605 	 Precision: 0.01226	 Recall: 0.09062	NDCG: 0.04958
The time for epoch 25 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.95740, F1-score: 0.021592 	 Precision: 0.01226	 Recall: 0.09015	NDCG: 0.04949
The time for epoch 26 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.01929, F1-score: 0.021592 	 Precision: 0.01226	 Recall: 0.09015	NDCG: 0.04922
The time for epoch 27 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.59799, F1-score: 0.021711 	 Precision: 0.01233	 Recall: 0.09054	NDCG: 0.04935
The time for epoch 28 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.53113, F1-score: 0.021596 	 Precision: 0.01226	 Recall: 0.09030	NDCG: 0.04935
The time for epoch 29 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.88748, F1-score: 0.021658 	 Precision: 0.01230	 Recall: 0.09058	NDCG: 0.04942
The time for epoch 30 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 270.77979, F1-score: 0.021589 	 Precision: 0.01226	 Recall: 0.09005	NDCG: 0.04921
The time for epoch 31 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.25992, F1-score: 0.021599 	 Precision: 0.01226	 Recall: 0.09040	NDCG: 0.04928
The time for epoch 32 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.53012, F1-score: 0.021597 	 Precision: 0.01226	 Recall: 0.09033	NDCG: 0.04926
The time for epoch 33 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.86038, F1-score: 0.021471 	 Precision: 0.01220	 Recall: 0.08969	NDCG: 0.04935
The time for epoch 34 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.66800, F1-score: 0.021532 	 Precision: 0.01223	 Recall: 0.08993	NDCG: 0.04919
The time for epoch 35 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.46936, F1-score: 0.021539 	 Precision: 0.01223	 Recall: 0.09019	NDCG: 0.04956
The time for epoch 36 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.54141, F1-score: 0.021359 	 Precision: 0.01213	 Recall: 0.08955	NDCG: 0.04927
The time for epoch 37 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.13730, F1-score: 0.021605 	 Precision: 0.01226	 Recall: 0.09060	NDCG: 0.04966
The time for epoch 38 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.09445, F1-score: 0.021537 	 Precision: 0.01223	 Recall: 0.09011	NDCG: 0.04953
The time for epoch 39 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.09357, F1-score: 0.021359 	 Precision: 0.01213	 Recall: 0.08957	NDCG: 0.04926
The time for epoch 40 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.80768, F1-score: 0.021601 	 Precision: 0.01226	 Recall: 0.09046	NDCG: 0.04957
The time for epoch 41 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.36295, F1-score: 0.021416 	 Precision: 0.01216	 Recall: 0.08965	NDCG: 0.04932
The time for epoch 42 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.21274, F1-score: 0.021601 	 Precision: 0.01226	 Recall: 0.09046	NDCG: 0.04934
The time for epoch 43 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 269.41983, F1-score: 0.021651 	 Precision: 0.01230	 Recall: 0.09032	NDCG: 0.04958
The time for epoch 44 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.72675, F1-score: 0.021530 	 Precision: 0.01223	 Recall: 0.08986	NDCG: 0.04941
The time for epoch 45 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.96143, F1-score: 0.021736 	 Precision: 0.01233	 Recall: 0.09140	NDCG: 0.04981
The time for epoch 46 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.40387, F1-score: 0.021727 	 Precision: 0.01233	 Recall: 0.09108	NDCG: 0.04954
The time for epoch 47 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.28503, F1-score: 0.021599 	 Precision: 0.01226	 Recall: 0.09039	NDCG: 0.04966
The time for epoch 48 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.10150, F1-score: 0.021658 	 Precision: 0.01230	 Recall: 0.09056	NDCG: 0.04961
The time for epoch 49 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.31256, F1-score: 0.021532 	 Precision: 0.01223	 Recall: 0.08994	NDCG: 0.04917
The time for epoch 50 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.84085, F1-score: 0.021773 	 Precision: 0.01237	 Recall: 0.09081	NDCG: 0.04972
The time for epoch 51 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.68051, F1-score: 0.021716 	 Precision: 0.01233	 Recall: 0.09072	NDCG: 0.04978
The time for epoch 52 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.10791, F1-score: 0.021537 	 Precision: 0.01223	 Recall: 0.09011	NDCG: 0.04957
The time for epoch 53 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.48328, F1-score: 0.021473 	 Precision: 0.01220	 Recall: 0.08978	NDCG: 0.04944
The time for epoch 54 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.26785, F1-score: 0.021420 	 Precision: 0.01216	 Recall: 0.08979	NDCG: 0.04943
The time for epoch 55 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.69580, F1-score: 0.021429 	 Precision: 0.01216	 Recall: 0.09012	NDCG: 0.04950
The time for epoch 56 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.02289, F1-score: 0.021426 	 Precision: 0.01216	 Recall: 0.09000	NDCG: 0.04943
The time for epoch 57 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.34964, F1-score: 0.021657 	 Precision: 0.01230	 Recall: 0.09052	NDCG: 0.04959
The time for epoch 58 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.73715, F1-score: 0.021728 	 Precision: 0.01233	 Recall: 0.09113	NDCG: 0.04958
The time for epoch 59 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.52292, F1-score: 0.021536 	 Precision: 0.01223	 Recall: 0.09008	NDCG: 0.04919
The time for epoch 60 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.66681, F1-score: 0.021538 	 Precision: 0.01223	 Recall: 0.09014	NDCG: 0.04920
The time for epoch 61 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.84027, F1-score: 0.021779 	 Precision: 0.01237	 Recall: 0.09101	NDCG: 0.04951
The time for epoch 62 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.41571, F1-score: 0.021608 	 Precision: 0.01226	 Recall: 0.09070	NDCG: 0.04943
The time for epoch 63 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.78162, F1-score: 0.021718 	 Precision: 0.01233	 Recall: 0.09079	NDCG: 0.04949
The time for epoch 64 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.05856, F1-score: 0.021418 	 Precision: 0.01216	 Recall: 0.08974	NDCG: 0.04934
The time for epoch 65 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.62723, F1-score: 0.021416 	 Precision: 0.01216	 Recall: 0.08966	NDCG: 0.04933
The time for epoch 66 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.81924, F1-score: 0.021530 	 Precision: 0.01223	 Recall: 0.08986	NDCG: 0.04949
The time for epoch 67 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.53543, F1-score: 0.021535 	 Precision: 0.01223	 Recall: 0.09004	NDCG: 0.04953
The time for epoch 68 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.72391, F1-score: 0.021364 	 Precision: 0.01213	 Recall: 0.08974	NDCG: 0.04931
The time for epoch 69 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.30157, F1-score: 0.021587 	 Precision: 0.01226	 Recall: 0.08998	NDCG: 0.04945
The time for epoch 70 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.93915, F1-score: 0.021479 	 Precision: 0.01220	 Recall: 0.08997	NDCG: 0.04941
The time for epoch 71 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.16559, F1-score: 0.021737 	 Precision: 0.01233	 Recall: 0.09145	NDCG: 0.05005
The time for epoch 72 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 271.02606, F1-score: 0.021777 	 Precision: 0.01237	 Recall: 0.09096	NDCG: 0.04974
The time for epoch 73 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.04446, F1-score: 0.021910 	 Precision: 0.01244	 Recall: 0.09183	NDCG: 0.05006
The time for epoch 74 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.53766, F1-score: 0.021667 	 Precision: 0.01230	 Recall: 0.09087	NDCG: 0.04949
The time for epoch 75 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.24994, F1-score: 0.021795 	 Precision: 0.01237	 Recall: 0.09157	NDCG: 0.04968
The time for epoch 76 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.83279, F1-score: 0.021790 	 Precision: 0.01237	 Recall: 0.09142	NDCG: 0.04964
The time for epoch 77 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.30423, F1-score: 0.021733 	 Precision: 0.01233	 Recall: 0.09130	NDCG: 0.04975
The time for epoch 78 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 275.50732, F1-score: 0.021733 	 Precision: 0.01233	 Recall: 0.09130	NDCG: 0.04985
The time for epoch 79 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.91949, F1-score: 0.021847 	 Precision: 0.01240	 Recall: 0.09151	NDCG: 0.04990
The time for epoch 80 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.26782, F1-score: 0.021727 	 Precision: 0.01233	 Recall: 0.09108	NDCG: 0.04974
The time for epoch 81 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.83939, F1-score: 0.021599 	 Precision: 0.01226	 Recall: 0.09040	NDCG: 0.04964
The time for epoch 82 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.61542, F1-score: 0.021659 	 Precision: 0.01230	 Recall: 0.09059	NDCG: 0.04972
The time for epoch 83 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.88766, F1-score: 0.021672 	 Precision: 0.01230	 Recall: 0.09105	NDCG: 0.04971
The time for epoch 84 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.86041, F1-score: 0.021607 	 Precision: 0.01226	 Recall: 0.09066	NDCG: 0.04961
The time for epoch 85 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.54675, F1-score: 0.021476 	 Precision: 0.01220	 Recall: 0.08989	NDCG: 0.04948
The time for epoch 86 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.04297, F1-score: 0.021484 	 Precision: 0.01220	 Recall: 0.09014	NDCG: 0.04952
The time for epoch 87 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 270.11917, F1-score: 0.021728 	 Precision: 0.01233	 Recall: 0.09112	NDCG: 0.04974
The time for epoch 88 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.39755, F1-score: 0.021421 	 Precision: 0.01216	 Recall: 0.08982	NDCG: 0.04911
The time for epoch 89 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.35654, F1-score: 0.021590 	 Precision: 0.01226	 Recall: 0.09010	NDCG: 0.04930
The time for epoch 90 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.47672, F1-score: 0.021733 	 Precision: 0.01233	 Recall: 0.09132	NDCG: 0.04977
The time for epoch 91 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.27734, F1-score: 0.021743 	 Precision: 0.01233	 Recall: 0.09164	NDCG: 0.04994
The time for epoch 92 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.28925, F1-score: 0.021462 	 Precision: 0.01220	 Recall: 0.08938	NDCG: 0.04940
The time for epoch 93 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.26865, F1-score: 0.021414 	 Precision: 0.01216	 Recall: 0.08957	NDCG: 0.04938
The time for epoch 94 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.29874, F1-score: 0.021364 	 Precision: 0.01213	 Recall: 0.08974	NDCG: 0.04904
The time for epoch 95 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.90451, F1-score: 0.021851 	 Precision: 0.01240	 Recall: 0.09164	NDCG: 0.04989
The time for epoch 96 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.83261, F1-score: 0.021962 	 Precision: 0.01247	 Recall: 0.09174	NDCG: 0.04994
The time for epoch 97 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.42194, F1-score: 0.021906 	 Precision: 0.01244	 Recall: 0.09168	NDCG: 0.05001
The time for epoch 98 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.75388, F1-score: 0.021726 	 Precision: 0.01233	 Recall: 0.09105	NDCG: 0.04985
The time for epoch 99 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.57251, F1-score: 0.021605 	 Precision: 0.01226	 Recall: 0.09061	NDCG: 0.04967
The time for epoch 100 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.34793, F1-score: 0.022078 	 Precision: 0.01254	 Recall: 0.09204	NDCG: 0.05010
The time for epoch 101 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.23853, F1-score: 0.021421 	 Precision: 0.01216	 Recall: 0.08983	NDCG: 0.04942
The time for epoch 102 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.49014, F1-score: 0.021585 	 Precision: 0.01226	 Recall: 0.08992	NDCG: 0.04918
The time for epoch 103 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.40952, F1-score: 0.021544 	 Precision: 0.01223	 Recall: 0.09037	NDCG: 0.04952
The time for epoch 104 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.53168, F1-score: 0.021476 	 Precision: 0.01220	 Recall: 0.08989	NDCG: 0.04946
The time for epoch 105 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.83191, F1-score: 0.021602 	 Precision: 0.01226	 Recall: 0.09050	NDCG: 0.04929
The time for epoch 106 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.26428, F1-score: 0.021672 	 Precision: 0.01230	 Recall: 0.09105	NDCG: 0.04943
The time for epoch 107 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.21381, F1-score: 0.021785 	 Precision: 0.01237	 Recall: 0.09122	NDCG: 0.04986
The time for epoch 108 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.87280, F1-score: 0.021672 	 Precision: 0.01230	 Recall: 0.09105	NDCG: 0.04969
The time for epoch 109 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.68033, F1-score: 0.021731 	 Precision: 0.01233	 Recall: 0.09123	NDCG: 0.04952
The time for epoch 110 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.08322, F1-score: 0.021536 	 Precision: 0.01223	 Recall: 0.09007	NDCG: 0.04945
The time for epoch 111 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.50885, F1-score: 0.021851 	 Precision: 0.01240	 Recall: 0.09166	NDCG: 0.04989
The time for epoch 112 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.28613, F1-score: 0.021726 	 Precision: 0.01233	 Recall: 0.09107	NDCG: 0.04952
The time for epoch 113 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.69244, F1-score: 0.021767 	 Precision: 0.01237	 Recall: 0.09062	NDCG: 0.04976
The time for epoch 114 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.22836, F1-score: 0.021658 	 Precision: 0.01230	 Recall: 0.09058	NDCG: 0.04958
The time for epoch 115 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 271.42484, F1-score: 0.021603 	 Precision: 0.01226	 Recall: 0.09055	NDCG: 0.04967
The time for epoch 116 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.83270, F1-score: 0.021590 	 Precision: 0.01226	 Recall: 0.09010	NDCG: 0.04948
The time for epoch 117 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.49570, F1-score: 0.021601 	 Precision: 0.01226	 Recall: 0.09046	NDCG: 0.04956
The time for epoch 118 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.69458, F1-score: 0.021723 	 Precision: 0.01233	 Recall: 0.09096	NDCG: 0.04975
The time for epoch 119 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.45984, F1-score: 0.021480 	 Precision: 0.01220	 Recall: 0.09000	NDCG: 0.04923
The time for epoch 120 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.50797, F1-score: 0.021484 	 Precision: 0.01220	 Recall: 0.09014	NDCG: 0.04926
The time for epoch 121 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.89032, F1-score: 0.021544 	 Precision: 0.01223	 Recall: 0.09037	NDCG: 0.04953
The time for epoch 122 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.75320, F1-score: 0.021716 	 Precision: 0.01233	 Recall: 0.09069	NDCG: 0.04968
The time for epoch 123 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.92679, F1-score: 0.021720 	 Precision: 0.01233	 Recall: 0.09084	NDCG: 0.04975
The time for epoch 124 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.85666, F1-score: 0.021669 	 Precision: 0.01230	 Recall: 0.09097	NDCG: 0.04976
The time for epoch 125 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.62622, F1-score: 0.022012 	 Precision: 0.01251	 Recall: 0.09162	NDCG: 0.05005
The time for epoch 126 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.88977, F1-score: 0.021526 	 Precision: 0.01223	 Recall: 0.08973	NDCG: 0.04944
The time for epoch 127 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.52771, F1-score: 0.021356 	 Precision: 0.01213	 Recall: 0.08946	NDCG: 0.04933
The time for epoch 128 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.07327, F1-score: 0.021556 	 Precision: 0.01223	 Recall: 0.09080	NDCG: 0.04966
The time for epoch 129 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.46509, F1-score: 0.021490 	 Precision: 0.01220	 Recall: 0.09035	NDCG: 0.04930
The time for epoch 130 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.95224, F1-score: 0.021417 	 Precision: 0.01216	 Recall: 0.08971	NDCG: 0.04941
The time for epoch 131 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.36331, F1-score: 0.021539 	 Precision: 0.01223	 Recall: 0.09020	NDCG: 0.04957
The time for epoch 132 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 269.17670, F1-score: 0.021726 	 Precision: 0.01233	 Recall: 0.09105	NDCG: 0.04981
The time for epoch 133 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.91199, F1-score: 0.021662 	 Precision: 0.01230	 Recall: 0.09072	NDCG: 0.04965
The time for epoch 134 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.69107, F1-score: 0.021737 	 Precision: 0.01233	 Recall: 0.09145	NDCG: 0.04991
The time for epoch 135 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.32043, F1-score: 0.021594 	 Precision: 0.01226	 Recall: 0.09021	NDCG: 0.04952
The time for epoch 136 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.14377, F1-score: 0.021719 	 Precision: 0.01233	 Recall: 0.09082	NDCG: 0.04977
The time for epoch 137 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.36523, F1-score: 0.021765 	 Precision: 0.01237	 Recall: 0.09052	NDCG: 0.04938
The time for epoch 138 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.74759, F1-score: 0.021835 	 Precision: 0.01240	 Recall: 0.09108	NDCG: 0.04947
The time for epoch 139 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.56003, F1-score: 0.021644 	 Precision: 0.01230	 Recall: 0.09007	NDCG: 0.04924
The time for epoch 140 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.90570, F1-score: 0.021560 	 Precision: 0.01223	 Recall: 0.09091	NDCG: 0.04964
The time for epoch 141 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 269.85153, F1-score: 0.021469 	 Precision: 0.01220	 Recall: 0.08963	NDCG: 0.04943
The time for epoch 142 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.63925, F1-score: 0.021719 	 Precision: 0.01233	 Recall: 0.09081	NDCG: 0.04979
The time for epoch 143 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 271.12875, F1-score: 0.021534 	 Precision: 0.01223	 Recall: 0.09000	NDCG: 0.04951
The time for epoch 144 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.60034, F1-score: 0.021976 	 Precision: 0.01247	 Recall: 0.09223	NDCG: 0.05015
The time for epoch 145 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.60321, F1-score: 0.021788 	 Precision: 0.01237	 Recall: 0.09133	NDCG: 0.04956
The time for epoch 146 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.86169, F1-score: 0.021838 	 Precision: 0.01240	 Recall: 0.09119	NDCG: 0.04961
The time for epoch 147 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.99182, F1-score: 0.021722 	 Precision: 0.01233	 Recall: 0.09090	NDCG: 0.04979
The time for epoch 148 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 271.99930, F1-score: 0.021533 	 Precision: 0.01223	 Recall: 0.08998	NDCG: 0.04917
The time for epoch 149 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.47076, F1-score: 0.021540 	 Precision: 0.01223	 Recall: 0.09021	NDCG: 0.04949
The time for epoch 150 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.71371, F1-score: 0.021793 	 Precision: 0.01237	 Recall: 0.09151	NDCG: 0.04985
The time for epoch 151 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.90906, F1-score: 0.021724 	 Precision: 0.01233	 Recall: 0.09099	NDCG: 0.04981
The time for epoch 152 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.34637, F1-score: 0.021652 	 Precision: 0.01230	 Recall: 0.09037	NDCG: 0.04969
The time for epoch 153 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.87164, F1-score: 0.021607 	 Precision: 0.01226	 Recall: 0.09067	NDCG: 0.04964
The time for epoch 154 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 254.31413, F1-score: 0.021660 	 Precision: 0.01230	 Recall: 0.09065	NDCG: 0.04944
The time for epoch 155 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.98386, F1-score: 0.021723 	 Precision: 0.01233	 Recall: 0.09094	NDCG: 0.04955
The time for epoch 156 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.94440, F1-score: 0.021652 	 Precision: 0.01230	 Recall: 0.09034	NDCG: 0.04945
The time for epoch 157 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.39731, F1-score: 0.021472 	 Precision: 0.01220	 Recall: 0.08972	NDCG: 0.04917
The time for epoch 158 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.37943, F1-score: 0.021776 	 Precision: 0.01237	 Recall: 0.09090	NDCG: 0.04949
The time for epoch 159 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.16306, F1-score: 0.021654 	 Precision: 0.01230	 Recall: 0.09044	NDCG: 0.04933
The time for epoch 160 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.16061, F1-score: 0.021773 	 Precision: 0.01237	 Recall: 0.09080	NDCG: 0.04949
The time for epoch 161 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.64911, F1-score: 0.021553 	 Precision: 0.01223	 Recall: 0.09068	NDCG: 0.04941
The time for epoch 162 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.13080, F1-score: 0.021713 	 Precision: 0.01233	 Recall: 0.09058	NDCG: 0.04937
The time for epoch 163 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.43845, F1-score: 0.021530 	 Precision: 0.01223	 Recall: 0.08986	NDCG: 0.04943
The time for epoch 164 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 271.00104, F1-score: 0.021790 	 Precision: 0.01237	 Recall: 0.09141	NDCG: 0.04987
The time for epoch 165 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 269.25983, F1-score: 0.021590 	 Precision: 0.01226	 Recall: 0.09008	NDCG: 0.04942
The time for epoch 166 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.87521, F1-score: 0.021679 	 Precision: 0.01230	 Recall: 0.09130	NDCG: 0.04979
The time for epoch 167 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.44284, F1-score: 0.021808 	 Precision: 0.01237	 Recall: 0.09204	NDCG: 0.04999
The time for epoch 168 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.29639, F1-score: 0.021856 	 Precision: 0.01240	 Recall: 0.09184	NDCG: 0.05009
The time for epoch 169 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.68173, F1-score: 0.021830 	 Precision: 0.01240	 Recall: 0.09091	NDCG: 0.05034
The time for epoch 170 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.04062, F1-score: 0.021768 	 Precision: 0.01237	 Recall: 0.09063	NDCG: 0.04979
The time for epoch 171 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.99060, F1-score: 0.021790 	 Precision: 0.01237	 Recall: 0.09141	NDCG: 0.04964
The time for epoch 172 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 267.02954, F1-score: 0.021784 	 Precision: 0.01237	 Recall: 0.09120	NDCG: 0.04960
The time for epoch 173 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.51791, F1-score: 0.022088 	 Precision: 0.01254	 Recall: 0.09240	NDCG: 0.05011
The time for epoch 174 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.78574, F1-score: 0.021775 	 Precision: 0.01237	 Recall: 0.09087	NDCG: 0.04978
The time for epoch 175 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.51303, F1-score: 0.021791 	 Precision: 0.01237	 Recall: 0.09145	NDCG: 0.04999
The time for epoch 176 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.67050, F1-score: 0.021839 	 Precision: 0.01240	 Recall: 0.09125	NDCG: 0.05003
The time for epoch 177 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.51959, F1-score: 0.022191 	 Precision: 0.01261	 Recall: 0.09220	NDCG: 0.05029
The time for epoch 178 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.47498, F1-score: 0.022153 	 Precision: 0.01258	 Recall: 0.09277	NDCG: 0.05048
The time for epoch 179 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.74771, F1-score: 0.022091 	 Precision: 0.01254	 Recall: 0.09248	NDCG: 0.05029
The time for epoch 180 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.44333, F1-score: 0.022259 	 Precision: 0.01265	 Recall: 0.09269	NDCG: 0.05039
The time for epoch 181 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.30847, F1-score: 0.022073 	 Precision: 0.01254	 Recall: 0.09187	NDCG: 0.05016
The time for epoch 182 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.55045, F1-score: 0.022200 	 Precision: 0.01261	 Recall: 0.09254	NDCG: 0.05014
The time for epoch 183 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.49841, F1-score: 0.022262 	 Precision: 0.01265	 Recall: 0.09278	NDCG: 0.05043
The time for epoch 184 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.84460, F1-score: 0.021683 	 Precision: 0.01230	 Recall: 0.09144	NDCG: 0.04993
The time for epoch 185 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.48911, F1-score: 0.022352 	 Precision: 0.01268	 Recall: 0.09406	NDCG: 0.05078
The time for epoch 186 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.63980, F1-score: 0.022188 	 Precision: 0.01258	 Recall: 0.09401	NDCG: 0.05058
The time for epoch 187 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.58871, F1-score: 0.022213 	 Precision: 0.01261	 Recall: 0.09296	NDCG: 0.05067
The time for epoch 188 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.33511, F1-score: 0.022455 	 Precision: 0.01275	 Recall: 0.09387	NDCG: 0.05100
The time for epoch 189 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.10104, F1-score: 0.022208 	 Precision: 0.01261	 Recall: 0.09279	NDCG: 0.05059
The time for epoch 190 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.55420, F1-score: 0.022397 	 Precision: 0.01272	 Recall: 0.09374	NDCG: 0.05102
The time for epoch 191 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.08191, F1-score: 0.022462 	 Precision: 0.01275	 Recall: 0.09412	NDCG: 0.05108
The time for epoch 192 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.25479, F1-score: 0.022215 	 Precision: 0.01261	 Recall: 0.09303	NDCG: 0.05066
The time for epoch 193 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.97568, F1-score: 0.022517 	 Precision: 0.01279	 Recall: 0.09418	NDCG: 0.05122
The time for epoch 194 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.40506, F1-score: 0.022216 	 Precision: 0.01261	 Recall: 0.09307	NDCG: 0.05094
The time for epoch 195 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 266.56143, F1-score: 0.023025 	 Precision: 0.01307	 Recall: 0.09680	NDCG: 0.05206
The time for epoch 196 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.67010, F1-score: 0.022777 	 Precision: 0.01293	 Recall: 0.09570	NDCG: 0.05157
The time for epoch 197 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.34204, F1-score: 0.022904 	 Precision: 0.01300	 Recall: 0.09638	NDCG: 0.05184
The time for epoch 198 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.35663, F1-score: 0.022906 	 Precision: 0.01300	 Recall: 0.09643	NDCG: 0.05184
The time for epoch 199 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.27606, F1-score: 0.022958 	 Precision: 0.01303	 Recall: 0.09635	NDCG: 0.05171
The time for epoch 200 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.98090, F1-score: 0.022967 	 Precision: 0.01303	 Recall: 0.09667	NDCG: 0.05194
The time for epoch 201 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.53204, F1-score: 0.022892 	 Precision: 0.01300	 Recall: 0.09596	NDCG: 0.05187
The time for epoch 202 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 271.07651, F1-score: 0.023063 	 Precision: 0.01310	 Recall: 0.09626	NDCG: 0.05226
The time for epoch 203 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.56113, F1-score: 0.022849 	 Precision: 0.01296	 Recall: 0.09633	NDCG: 0.05234
The time for epoch 204 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 263.43973, F1-score: 0.022955 	 Precision: 0.01303	 Recall: 0.09625	NDCG: 0.05215
The time for epoch 205 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.51202, F1-score: 0.023122 	 Precision: 0.01314	 Recall: 0.09645	NDCG: 0.05208
The time for epoch 206 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.56812, F1-score: 0.023067 	 Precision: 0.01310	 Recall: 0.09640	NDCG: 0.05241
The time for epoch 207 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.06165, F1-score: 0.022954 	 Precision: 0.01303	 Recall: 0.09624	NDCG: 0.05246
The time for epoch 208 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 256.34250, F1-score: 0.023127 	 Precision: 0.01314	 Recall: 0.09661	NDCG: 0.05260
The time for epoch 209 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.38333, F1-score: 0.023308 	 Precision: 0.01324	 Recall: 0.09728	NDCG: 0.05316
The time for epoch 210 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.99780, F1-score: 0.023118 	 Precision: 0.01314	 Recall: 0.09629	NDCG: 0.05318
The time for epoch 211 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.15091, F1-score: 0.023797 	 Precision: 0.01352	 Recall: 0.09924	NDCG: 0.05396
The time for epoch 212 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.81999, F1-score: 0.023680 	 Precision: 0.01345	 Recall: 0.09893	NDCG: 0.05399
The time for epoch 213 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.88406, F1-score: 0.023538 	 Precision: 0.01338	 Recall: 0.09775	NDCG: 0.05403
The time for epoch 214 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.38284, F1-score: 0.023504 	 Precision: 0.01334	 Recall: 0.09847	NDCG: 0.05397
The time for epoch 215 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.80182, F1-score: 0.023788 	 Precision: 0.01352	 Recall: 0.09894	NDCG: 0.05438
The time for epoch 216 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 255.21666, F1-score: 0.023616 	 Precision: 0.01341	 Recall: 0.09860	NDCG: 0.05436
The time for epoch 217 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 264.13715, F1-score: 0.023853 	 Precision: 0.01355	 Recall: 0.09933	NDCG: 0.05465
The time for epoch 218 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.38736, F1-score: 0.023923 	 Precision: 0.01359	 Recall: 0.09988	NDCG: 0.05515
The time for epoch 219 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.94604, F1-score: 0.024147 	 Precision: 0.01373	 Recall: 0.10016	NDCG: 0.05567
The time for epoch 220 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.57921, F1-score: 0.024108 	 Precision: 0.01369	 Recall: 0.10067	NDCG: 0.05550
The time for epoch 221 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.78403, F1-score: 0.024412 	 Precision: 0.01387	 Recall: 0.10187	NDCG: 0.05634
The time for epoch 222 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.19867, F1-score: 0.024657 	 Precision: 0.01401	 Recall: 0.10288	NDCG: 0.05671
The time for epoch 223 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.23108, F1-score: 0.024361 	 Precision: 0.01383	 Recall: 0.10199	NDCG: 0.05645
The time for epoch 224 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 268.51135, F1-score: 0.024480 	 Precision: 0.01390	 Recall: 0.10237	NDCG: 0.05668
The time for epoch 225 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.49973, F1-score: 0.024229 	 Precision: 0.01376	 Recall: 0.10115	NDCG: 0.05680
The time for epoch 226 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 255.59575, F1-score: 0.024665 	 Precision: 0.01401	 Recall: 0.10317	NDCG: 0.05770
The time for epoch 227 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.35690, F1-score: 0.024704 	 Precision: 0.01404	 Recall: 0.10264	NDCG: 0.05741
The time for epoch 228 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 265.22263, F1-score: 0.024905 	 Precision: 0.01415	 Recall: 0.10398	NDCG: 0.05812
The time for epoch 229 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 256.44040, F1-score: 0.024860 	 Precision: 0.01411	 Recall: 0.10433	NDCG: 0.05829
The time for epoch 230 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.93518, F1-score: 0.024770 	 Precision: 0.01408	 Recall: 0.10307	NDCG: 0.05823
The time for epoch 231 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 251.86740, F1-score: 0.025143 	 Precision: 0.01429	 Recall: 0.10478	NDCG: 0.05907
The time for epoch 232 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 261.40088, F1-score: 0.024795 	 Precision: 0.01408	 Recall: 0.10395	NDCG: 0.05952
The time for epoch 233 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 252.09100, F1-score: 0.025041 	 Precision: 0.01422	 Recall: 0.10499	NDCG: 0.05984
The time for epoch 234 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 262.81711, F1-score: 0.025104 	 Precision: 0.01425	 Recall: 0.10530	NDCG: 0.06001
The time for epoch 235 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 260.77634, F1-score: 0.025172 	 Precision: 0.01429	 Recall: 0.10577	NDCG: 0.06041
The time for epoch 236 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 259.65402, F1-score: 0.025349 	 Precision: 0.01439	 Recall: 0.10629	NDCG: 0.06100
The time for epoch 237 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 255.21243, F1-score: 0.025358 	 Precision: 0.01439	 Recall: 0.10663	NDCG: 0.06139
The time for epoch 238 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.69189, F1-score: 0.025976 	 Precision: 0.01474	 Recall: 0.10933	NDCG: 0.06228
The time for epoch 239 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.81894, F1-score: 0.025901 	 Precision: 0.01470	 Recall: 0.10861	NDCG: 0.06210
The time for epoch 240 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 258.79630, F1-score: 0.025949 	 Precision: 0.01474	 Recall: 0.10838	NDCG: 0.06221
The time for epoch 241 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.44687, F1-score: 0.025590 	 Precision: 0.01453	 Recall: 0.10719	NDCG: 0.06230
The time for epoch 242 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 257.81552, F1-score: 0.026017 	 Precision: 0.01477	 Recall: 0.10889	NDCG: 0.06308
The time for epoch 243 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 250.66576, F1-score: 0.026464 	 Precision: 0.01502	 Recall: 0.11128	NDCG: 0.06395
The time for epoch 244 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 252.60826, F1-score: 0.026700 	 Precision: 0.01516	 Recall: 0.11201	NDCG: 0.06443
The time for epoch 245 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 256.64804, F1-score: 0.026897 	 Precision: 0.01526	 Recall: 0.11323	NDCG: 0.06544
The time for epoch 246 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 252.09659, F1-score: 0.027077 	 Precision: 0.01537	 Recall: 0.11386	NDCG: 0.06545
The time for epoch 247 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.31387, F1-score: 0.027106 	 Precision: 0.01540	 Recall: 0.11297	NDCG: 0.06656
The time for epoch 248 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 251.95700, F1-score: 0.027243 	 Precision: 0.01547	 Recall: 0.11399	NDCG: 0.06653
The time for epoch 249 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 249.57666, F1-score: 0.027366 	 Precision: 0.01554	 Recall: 0.11452	NDCG: 0.06714
The time for epoch 250 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 255.23816, F1-score: 0.027922 	 Precision: 0.01585	 Recall: 0.11695	NDCG: 0.06827
The time for epoch 251 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 250.21513, F1-score: 0.028046 	 Precision: 0.01592	 Recall: 0.11749	NDCG: 0.06904
The time for epoch 252 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 251.60466, F1-score: 0.027948 	 Precision: 0.01585	 Recall: 0.11785	NDCG: 0.06900
The time for epoch 253 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 250.99594, F1-score: 0.027868 	 Precision: 0.01582	 Recall: 0.11695	NDCG: 0.06939
The time for epoch 254 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 249.35612, F1-score: 0.028197 	 Precision: 0.01599	 Recall: 0.11901	NDCG: 0.06932
The time for epoch 255 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 246.60379, F1-score: 0.028265 	 Precision: 0.01603	 Recall: 0.11949	NDCG: 0.06939
The time for epoch 256 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 252.47614, F1-score: 0.028465 	 Precision: 0.01613	 Recall: 0.12084	NDCG: 0.07019
The time for epoch 257 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 249.27466, F1-score: 0.028657 	 Precision: 0.01624	 Recall: 0.12189	NDCG: 0.07104
The time for epoch 258 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 248.09573, F1-score: 0.028262 	 Precision: 0.01603	 Recall: 0.11938	NDCG: 0.07046
The time for epoch 259 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 245.94283, F1-score: 0.028870 	 Precision: 0.01638	 Recall: 0.12178	NDCG: 0.07150
The time for epoch 260 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 249.24078, F1-score: 0.028985 	 Precision: 0.01645	 Recall: 0.12202	NDCG: 0.07178
The time for epoch 261 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 246.63902, F1-score: 0.029053 	 Precision: 0.01648	 Recall: 0.12251	NDCG: 0.07211
The time for epoch 262 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 247.18103, F1-score: 0.029487 	 Precision: 0.01672	 Recall: 0.12445	NDCG: 0.07270
The time for epoch 263 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 242.46178, F1-score: 0.029276 	 Precision: 0.01662	 Recall: 0.12272	NDCG: 0.07251
The time for epoch 264 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 245.08057, F1-score: 0.029434 	 Precision: 0.01669	 Recall: 0.12451	NDCG: 0.07252
The time for epoch 265 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 253.41521, F1-score: 0.029533 	 Precision: 0.01676	 Recall: 0.12416	NDCG: 0.07308
The time for epoch 266 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 237.92856, F1-score: 0.029533 	 Precision: 0.01676	 Recall: 0.12416	NDCG: 0.07329
The time for epoch 267 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 242.75240, F1-score: 0.029596 	 Precision: 0.01679	 Recall: 0.12447	NDCG: 0.07407
The time for epoch 268 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 246.55788, F1-score: 0.029825 	 Precision: 0.01693	 Recall: 0.12494	NDCG: 0.07367
The time for epoch 269 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 245.15053, F1-score: 0.030085 	 Precision: 0.01707	 Recall: 0.12646	NDCG: 0.07465
The time for epoch 270 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 240.63457, F1-score: 0.030274 	 Precision: 0.01718	 Recall: 0.12740	NDCG: 0.07505
The time for epoch 271 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 242.29622, F1-score: 0.029875 	 Precision: 0.01697	 Recall: 0.12479	NDCG: 0.07453
The time for epoch 272 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 247.27490, F1-score: 0.030263 	 Precision: 0.01718	 Recall: 0.12702	NDCG: 0.07518
The time for epoch 273 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 239.82414, F1-score: 0.030375 	 Precision: 0.01725	 Recall: 0.12715	NDCG: 0.07542
The time for epoch 274 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 239.88318, F1-score: 0.030394 	 Precision: 0.01725	 Recall: 0.12785	NDCG: 0.07635
The time for epoch 275 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 235.87129, F1-score: 0.030327 	 Precision: 0.01721	 Recall: 0.12737	NDCG: 0.07599
The time for epoch 276 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 239.75816, F1-score: 0.030446 	 Precision: 0.01728	 Recall: 0.12775	NDCG: 0.07620
The time for epoch 277 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 227.79428, F1-score: 0.030236 	 Precision: 0.01718	 Recall: 0.12607	NDCG: 0.07588
The time for epoch 278 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 234.26358, F1-score: 0.030836 	 Precision: 0.01753	 Recall: 0.12818	NDCG: 0.07661
The time for epoch 279 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 237.86842, F1-score: 0.030833 	 Precision: 0.01753	 Recall: 0.12809	NDCG: 0.07641
The time for epoch 280 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 236.24072, F1-score: 0.030963 	 Precision: 0.01760	 Recall: 0.12884	NDCG: 0.07672
The time for epoch 281 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 238.77925, F1-score: 0.030694 	 Precision: 0.01746	 Recall: 0.12699	NDCG: 0.07621
The time for epoch 282 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 235.15942, F1-score: 0.030888 	 Precision: 0.01756	 Recall: 0.12810	NDCG: 0.07717
The time for epoch 283 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 237.72559, F1-score: 0.031464 	 Precision: 0.01791	 Recall: 0.12941	NDCG: 0.07759
The time for epoch 284 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 234.20084, F1-score: 0.031332 	 Precision: 0.01784	 Recall: 0.12858	NDCG: 0.07724
The time for epoch 285 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 226.63675, F1-score: 0.031394 	 Precision: 0.01787	 Recall: 0.12884	NDCG: 0.07790
The time for epoch 286 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 225.82613, F1-score: 0.031445 	 Precision: 0.01791	 Recall: 0.12874	NDCG: 0.07760
The time for epoch 287 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 231.17947, F1-score: 0.031698 	 Precision: 0.01805	 Recall: 0.13004	NDCG: 0.07785
The time for epoch 288 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 230.66553, F1-score: 0.031655 	 Precision: 0.01801	 Recall: 0.13039	NDCG: 0.07837
The time for epoch 289 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 229.33214, F1-score: 0.031806 	 Precision: 0.01812	 Recall: 0.13007	NDCG: 0.07866
The time for epoch 290 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 231.35359, F1-score: 0.031771 	 Precision: 0.01808	 Recall: 0.13068	NDCG: 0.07837
The time for epoch 291 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 229.12997, F1-score: 0.031942 	 Precision: 0.01819	 Recall: 0.13103	NDCG: 0.07874
The time for epoch 292 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 226.49695, F1-score: 0.032069 	 Precision: 0.01826	 Recall: 0.13168	NDCG: 0.07936
The time for epoch 293 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 221.83615, F1-score: 0.032003 	 Precision: 0.01822	 Recall: 0.13124	NDCG: 0.07915
The time for epoch 294 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 220.93399, F1-score: 0.031648 	 Precision: 0.01801	 Recall: 0.13015	NDCG: 0.07976
The time for epoch 295 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 219.50891, F1-score: 0.031782 	 Precision: 0.01808	 Recall: 0.13105	NDCG: 0.07979
The time for epoch 296 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 222.09030, F1-score: 0.031847 	 Precision: 0.01812	 Recall: 0.13143	NDCG: 0.07979
The time for epoch 297 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 221.14377, F1-score: 0.032017 	 Precision: 0.01822	 Recall: 0.13174	NDCG: 0.07948
The time for epoch 298 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 221.33363, F1-score: 0.031916 	 Precision: 0.01815	 Recall: 0.13196	NDCG: 0.07979
The time for epoch 299 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 221.30783, F1-score: 0.031859 	 Precision: 0.01812	 Recall: 0.13186	NDCG: 0.07951
The time for epoch 300 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 214.24750, F1-score: 0.032400 	 Precision: 0.01843	 Recall: 0.13377	NDCG: 0.08033
The time for epoch 301 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 219.66551, F1-score: 0.032417 	 Precision: 0.01843	 Recall: 0.13437	NDCG: 0.08081
The time for epoch 302 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 215.19980, F1-score: 0.032291 	 Precision: 0.01836	 Recall: 0.13373	NDCG: 0.08036
The time for epoch 303 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 207.55661, F1-score: 0.032522 	 Precision: 0.01850	 Recall: 0.13425	NDCG: 0.08067
The time for epoch 304 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 210.30611, F1-score: 0.032823 	 Precision: 0.01868	 Recall: 0.13535	NDCG: 0.08083
The time for epoch 305 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 206.83716, F1-score: 0.032829 	 Precision: 0.01868	 Recall: 0.13557	NDCG: 0.08125
The time for epoch 306 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 206.66246, F1-score: 0.033018 	 Precision: 0.01878	 Recall: 0.13648	NDCG: 0.08183
The time for epoch 307 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 208.51439, F1-score: 0.032697 	 Precision: 0.01861	 Recall: 0.13472	NDCG: 0.08156
The time for epoch 308 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 206.28400, F1-score: 0.032631 	 Precision: 0.01857	 Recall: 0.13432	NDCG: 0.08155
The time for epoch 309 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 200.91974, F1-score: 0.032694 	 Precision: 0.01861	 Recall: 0.13462	NDCG: 0.08186
The time for epoch 310 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 201.61220, F1-score: 0.033028 	 Precision: 0.01878	 Recall: 0.13683	NDCG: 0.08285
The time for epoch 311 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 196.80103, F1-score: 0.032716 	 Precision: 0.01861	 Recall: 0.13537	NDCG: 0.08285
The time for epoch 312 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 199.78529, F1-score: 0.032449 	 Precision: 0.01847	 Recall: 0.13363	NDCG: 0.08198
The time for epoch 313 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 196.13338, F1-score: 0.032383 	 Precision: 0.01843	 Recall: 0.13319	NDCG: 0.08173
The time for epoch 314 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 192.92116, F1-score: 0.032526 	 Precision: 0.01850	 Recall: 0.13441	NDCG: 0.08171
The time for epoch 315 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 191.47200, F1-score: 0.032677 	 Precision: 0.01861	 Recall: 0.13405	NDCG: 0.08163
The time for epoch 316 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 194.99203, F1-score: 0.032939 	 Precision: 0.01875	 Recall: 0.13564	NDCG: 0.08210
The time for epoch 317 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 190.97472, F1-score: 0.032561 	 Precision: 0.01854	 Recall: 0.13378	NDCG: 0.08145
The time for epoch 318 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 188.25484, F1-score: 0.032700 	 Precision: 0.01861	 Recall: 0.13482	NDCG: 0.08155
The time for epoch 319 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 186.58264, F1-score: 0.032685 	 Precision: 0.01861	 Recall: 0.13434	NDCG: 0.08106
The time for epoch 320 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 181.82184, F1-score: 0.032481 	 Precision: 0.01850	 Recall: 0.13289	NDCG: 0.08041
The time for epoch 321 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 183.11710, F1-score: 0.032550 	 Precision: 0.01854	 Recall: 0.13339	NDCG: 0.08021
The time for epoch 322 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 179.23000, F1-score: 0.032430 	 Precision: 0.01847	 Recall: 0.13296	NDCG: 0.08011
The time for epoch 323 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 176.94046, F1-score: 0.032370 	 Precision: 0.01843	 Recall: 0.13275	NDCG: 0.07993
The time for epoch 324 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 176.69652, F1-score: 0.031925 	 Precision: 0.01819	 Recall: 0.13046	NDCG: 0.07903
The time for epoch 325 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 171.10252, F1-score: 0.031837 	 Precision: 0.01815	 Recall: 0.12930	NDCG: 0.07895
The time for epoch 326 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 169.21535, F1-score: 0.031908 	 Precision: 0.01819	 Recall: 0.12987	NDCG: 0.07884
The time for epoch 327 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 169.16731, F1-score: 0.031693 	 Precision: 0.01805	 Recall: 0.12987	NDCG: 0.07848
The time for epoch 328 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 166.80124, F1-score: 0.031375 	 Precision: 0.01787	 Recall: 0.12823	NDCG: 0.07768
The time for epoch 329 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 161.52255, F1-score: 0.031530 	 Precision: 0.01798	 Recall: 0.12802	NDCG: 0.07710
The time for epoch 330 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 160.96094, F1-score: 0.031355 	 Precision: 0.01787	 Recall: 0.12756	NDCG: 0.07733
The time for epoch 331 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 157.88774, F1-score: 0.031229 	 Precision: 0.01780	 Recall: 0.12691	NDCG: 0.07750
The time for epoch 332 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 155.74721, F1-score: 0.031175 	 Precision: 0.01777	 Recall: 0.12691	NDCG: 0.07738
The time for epoch 333 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 154.49652, F1-score: 0.030929 	 Precision: 0.01763	 Recall: 0.12586	NDCG: 0.07644
The time for epoch 334 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 155.15157, F1-score: 0.031030 	 Precision: 0.01770	 Recall: 0.12565	NDCG: 0.07573
The time for epoch 335 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 150.97318, F1-score: 0.030865 	 Precision: 0.01760	 Recall: 0.12553	NDCG: 0.07556
The time for epoch 336 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 152.37766, F1-score: 0.030815 	 Precision: 0.01756	 Recall: 0.12565	NDCG: 0.07527
The time for epoch 337 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 146.29514, F1-score: 0.030915 	 Precision: 0.01763	 Recall: 0.12539	NDCG: 0.07475
The time for epoch 338 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 146.30655, F1-score: 0.030905 	 Precision: 0.01763	 Recall: 0.12507	NDCG: 0.07472
The time for epoch 339 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 143.13283, F1-score: 0.030291 	 Precision: 0.01728	 Recall: 0.12250	NDCG: 0.07379
The time for epoch 340 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 142.84877, F1-score: 0.030381 	 Precision: 0.01732	 Recall: 0.12370	NDCG: 0.07334
The time for epoch 341 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 138.89090, F1-score: 0.029953 	 Precision: 0.01707	 Recall: 0.12194	NDCG: 0.07230
The time for epoch 342 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 143.18039, F1-score: 0.029704 	 Precision: 0.01693	 Recall: 0.12081	NDCG: 0.07175
The time for epoch 343 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 133.31259, F1-score: 0.029888 	 Precision: 0.01704	 Recall: 0.12157	NDCG: 0.07192
The time for epoch 344 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 136.87279, F1-score: 0.029839 	 Precision: 0.01700	 Recall: 0.12172	NDCG: 0.07156
The time for epoch 345 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 130.15030, F1-score: 0.029603 	 Precision: 0.01686	 Recall: 0.12101	NDCG: 0.07114
The time for epoch 346 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 130.15309, F1-score: 0.029815 	 Precision: 0.01700	 Recall: 0.12093	NDCG: 0.07133
The time for epoch 347 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 125.55536, F1-score: 0.029392 	 Precision: 0.01676	 Recall: 0.11936	NDCG: 0.07004
The time for epoch 348 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 125.38191, F1-score: 0.028933 	 Precision: 0.01652	 Recall: 0.11661	NDCG: 0.06905
The time for epoch 349 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 123.82457, F1-score: 0.029057 	 Precision: 0.01659	 Recall: 0.11716	NDCG: 0.06943
The time for epoch 350 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 122.90924, F1-score: 0.028897 	 Precision: 0.01648	 Recall: 0.11718	NDCG: 0.06928
The time for epoch 351 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 121.75815, F1-score: 0.028434 	 Precision: 0.01624	 Recall: 0.11428	NDCG: 0.06788
The time for epoch 352 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 121.42481, F1-score: 0.028482 	 Precision: 0.01627	 Recall: 0.11412	NDCG: 0.06783
The time for epoch 353 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 116.36924, F1-score: 0.027894 	 Precision: 0.01592	 Recall: 0.11237	NDCG: 0.06691
The time for epoch 354 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 115.87682, F1-score: 0.028126 	 Precision: 0.01606	 Recall: 0.11295	NDCG: 0.06625
The time for epoch 355 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 116.22459, F1-score: 0.028061 	 Precision: 0.01603	 Recall: 0.11260	NDCG: 0.06614
The time for epoch 356 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 112.79930, F1-score: 0.027686 	 Precision: 0.01582	 Recall: 0.11084	NDCG: 0.06533
The time for epoch 357 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 106.54139, F1-score: 0.027643 	 Precision: 0.01578	 Recall: 0.11115	NDCG: 0.06490
The time for epoch 358 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 109.84360, F1-score: 0.027388 	 Precision: 0.01564	 Recall: 0.10984	NDCG: 0.06426
The time for epoch 359 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 108.80411, F1-score: 0.026938 	 Precision: 0.01540	 Recall: 0.10738	NDCG: 0.06353
The time for epoch 360 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 108.21702, F1-score: 0.026715 	 Precision: 0.01526	 Recall: 0.10707	NDCG: 0.06309
The time for epoch 361 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 104.88312, F1-score: 0.026216 	 Precision: 0.01498	 Recall: 0.10478	NDCG: 0.06183
The time for epoch 362 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 103.86857, F1-score: 0.026120 	 Precision: 0.01491	 Recall: 0.10512	NDCG: 0.06140
The time for epoch 363 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 104.33599, F1-score: 0.026168 	 Precision: 0.01495	 Recall: 0.10493	NDCG: 0.06137
The time for epoch 364 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 102.25384, F1-score: 0.025951 	 Precision: 0.01484	 Recall: 0.10311	NDCG: 0.06079
The time for epoch 365 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 100.90456, F1-score: 0.025698 	 Precision: 0.01467	 Recall: 0.10357	NDCG: 0.06052

The best result:
The time for epoch 310 is: train time = 00: 00: 03, test time = 00: 00: 00
Loss = 201.61220, F1-score: 0.033028 	 Precision: 0.01878	 Recall: 0.13683	NDCG: 0.08285

```
