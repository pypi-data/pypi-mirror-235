from hivesda import test
import os

# # setting cuda

device = "GPU"   # CPU or GPU
gpu = "0"        # set gpu numer
seed = 0         # fix seed
input_size = 300 # set image size e.g.) 300 -> (300x300)    
batch_size = 32   # set batch size
lr = 2e-4        # set learning-rate

# total train epoch = meta_epoch * sub_epoch
# start validation when end of sub_epochs
meta_epochs = 5 # set total_epoch
sub_epochs = 8   # set sub_epoch

output_dir = "./"
save_model_path = "../20231012.pt"
######################################################################################################################################################################
# set data
train_list = []
val_list = []
ng_list = []

train_normal_list = os.listdir("/workspace/Data_toptec_center_png300/bottle/train/good")
for t in train_normal_list:
    train_list.append(["/workspace/Data_toptec_center_png300/bottle/train/good/"+t,0,None,'good'])
val_normal_list = os.listdir("/workspace/Data_toptec_center_png300/bottle/test/good")
for v in val_normal_list:
    val_list.append(["/workspace/Data_toptec_center_png300/bottle/test/good/"+v,0,None,'good'])

total_ng_list = os.listdir("/workspace/Data_toptec_center_png300/bottle/test/NG")
for n in total_ng_list:
    ng_list.append(["/workspace/Data_toptec_center_png300/bottle/test/NG/"+n,1,"/workspace/Data_toptec_center_png300/bottle/ground_truth/NG/"+n.split(".")[0]+"_mask.png",'NG'])
train_list = train_list + ng_list[:30]
val_list = val_list + ng_list[30:]
######################################################################################################################################################################

img_auc, pix_auc, pix_pro = test.main_single()
print(f'Image-AUC: {img_auc}, Pixel-AUC: {pix_auc}, Pixel-PRO: {pix_pro}')


