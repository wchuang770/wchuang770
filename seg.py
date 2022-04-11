import pkuseg



seg = pkuseg.pkuseg(model_name='medicine',postag=True)  # 程序会自动下载所对应的细领域模型
pkuseg.train('./data/train_pos.txt','./data/test_pos.txt','./model',train_iter = 20, init_model = './model/')
