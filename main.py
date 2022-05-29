
import train, detect 
from types import SimpleNamespace
thisdict = {
    "save_dir": 'runs',
    "epochs":200,
    "batch_size": 2,
    "weights": '',
    "single_cls": False,
    "evolve" : False, 
    "data": 'data\coco128.yaml',
    "cfg": 'models\yolov5s.yaml',
    "resume": False,
    "noval": 'store_true', 
    "nosave":'store_true',
    "workers": 0,
    "freeze": [0],
    "imgsz" : 640,
    "optimizer": "SGD",
    "cos_lr": False,
    "sync_bn": 1,
    "cache": 'val',
    'rect':False,
    "rank": 1,
    "image_weights": False,
    "quad": False,
    "hyp": 'data\hyps\para.yaml',
    "project": "runs/train",
    "name": 'exp',
    'exist_ok': False,
    'device': 'cpu',
    'noplots': False,
    "noautoanchor": False,
    "label_smoothing": 0.0,
    'patience':100,
    "save-period":-1,
    "local_rank": -1,
    "entity": None,
    "upload_dataset": False,
    "bbox_interval": 1,
    "artifact_alias": "latest",
    "multi_scale": True,
    "save_period": 1
}


di = SimpleNamespace(**thisdict)
train.main(di)
di.weights= "runs\\train\\exp\\weights\\best.pt"
train.main(di)

for i in range(2,5,1):
    di.weights= "runs\\train\\exp"+str(i)+"\\weights\\best.pt"
    if(i==4):
        di.batch_size = 10
    train.main(di)


di.patience =300 
di.weights= "runs\\train\\exp5\\weights\\best.pt"
di.batch_size = 5
train.main(di)



import detect 
from types import SimpleNamespace
Test = {
    "weights": "runs\\train\\exp6\\weights\\last.pt",  # model.pt path(s)
    "source": "images\\images\\test",  # file/dir/URL/glob, 0 for webcam
    "data": 'data\coco128.yaml',  # dataset.yaml path
    "imgsz":(640,640),  # inference size (height, width)
    "conf_thres":0.4,  # confidence threshold
    "iou_thres":0.3,  # NMS IOU threshold
    "max_det":1000,  # maximum detections per image
    "device":'',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
    "view_img":True,  # show results
    "save_txt":True,  # save results to *.txt
    "save_conf":True,  # save confidences in --save-txt labels
    "save_crop":False,  # save cropped prediction boxes
    "nosave":False,  # do not save images/videos
    "classes":None,  # filter by class: --class 0, or --class 0 2 3
    "agnostic_nms":False,  # class-agnostic NMS
    "augment":False,  # augmented inference
    "visualize":False,  # visualize features
    "update":False,  # update all models
    "project":'runs/detect',  # save results to project/name
    "name":'exp',  # save results to project/name
    "exist_ok":False,  # existing project/name ok, do not increment
    "line_thickness":3,  # bounding box thickness (pixels)
    "hide_labels":False,  # hide labels
    "hide_conf":False,  # hide confidences
    "half":False,  # use FP16 half-precision inference
    "dnn":False,  # use OpenCV DNN for ONNX inference
}
test = SimpleNamespace(**Test)


detect.main(test)


    
