#coding=utf-8

from XEdu.hub import Workflow as wf
import cv2

def pose_infer_demo():
    # a = time.time()
    img = 'pose1.jpg' # 指定进行推理的图片路径
    pose = wf(task='wholebody133')# ,checkpoint="rtmpose-m-80e511.onnx") # 实例化mmpose模型

    result,img = pose.inference(data=img,img_type='pil') # 在CPU上进行推理
    pose.show(img)
    pose.save(img,"pimg_ou.png")
    
    result = pose.format_output(lang="zh")
    # print(result)

def video_infer_demo():
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("pose.mp4")
    
    pose = wf(task='body')
    det = wf(task='bodydetect')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        bboxs = det.inference(data=frame,thr=0.3) # 在CPU上进行推理
        img = frame
        for i in bboxs:
            keypoints,img =pose.inference(data=img,img_type='cv2',bbox=i) # 在CPU上进行推理
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release()
    cv2.destroyAllWindows()

def det_infer_demo():
    # a = time.time()
    from XEdu.hub import Workflow as wf
    img = 'pose4.jpg' # 指定进行推理的图片路径

    det = wf(task='bodydetect')#,checkpoint='rtmdet-acc0de.onnx')# ,checkpoint="rtmpose-m-80e511.onnx") # 实例化mmpose模型

    bboxs,im_ou = det.inference(data=img,img_type='cv2',thr=0.3,show=True) # 在CPU上进行推理
    # print(bboxs)
    det.save(im_ou,"im_ou_d.jpg")

    det.format_output(lang="de")
    # print(result)

def hand_video_demo():
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("pose.mp4")

    pose = wf(task='hand21')# ,checkpoint="rtmpose-m-80e511.onnx") # 实例化pose模型

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        keypoints,img =pose.inference(data=frame,img_type='cv2') # 在CPU上进行推理
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release()
    cv2.destroyAllWindows()

def coco_det_demo():
    img = 'ele.jpg' # 指定进行推理的图片路径
    det = wf(task='cocodetect') # 实例化mmpose模型

    result,img = det.inference(data=img,img_type='cv2',thr=0.2) # 在CPU上进行推理
    det.show(img)
    # det.save(img,"pimg_ou.png")
    
    re = det.format_output(lang="zh")

def face_det_demo():
    img = 'pose3.jpg' # 指定进行推理的图片路径
    # img = 'face2.jpeg' # 指定进行推理的图片路径

    det = wf(task='facedetect' )
    face = wf(task="face")

    result,img = det.inference(data=img,img_type='cv2') # 在CPU上进行推理
    det.show(img)
    for i in result:
        ky,img = face.inference(data=img, img_type="cv2",bbox=i)#,erase=False)
        face.show(img)
    
    # re = face.format_output(lang="zh")

def ocr_demo():
    img = 'ocr.jpg' # 指定进行推理的图片路径
    ocr = wf(task='ocr' )#,checkpoint="rtmdet-coco.onnx") # 实例化mmpose模型

    result,img = ocr.inference(data=img,img_type='pil',show=True) # 在CPU上进行推理
    # print(result)
    # ocr.show(img)
    ocr.save(img,"pimg_ou.png")
    
    re = ocr.format_output(lang="zh")

def mmedu_demo():

    mm = wf(task='mmedu',checkpoint="cls.onnx")
    result, img = mm.inference(data='ele.jpg',img_type='cv2',show=True)
    # mm.show(img)
    re = mm.format_output(lang="zh")

def basenn_demo():

    mm = wf(task='basenn',checkpoint="basenn/basenn_cd.onnx") # iris act 
    result = mm.inference(data='ele.jpg')
    re = mm.format_output(lang="zh")

def hand_det_demo():
    img = 'hand4.jpeg' # 指定进行推理的图片路径
    det = wf(task='handdetect') # 实例化mmpose模型
    hand = wf(task='hand')

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result,img = det.inference(data=frame,img_type='cv2',thr=0.3) # 在CPU上进行推理
        for i in result:
            ky, img = hand.inference(data=img, img_type='cv2',bbox=i)
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release()
    cv2.destroyAllWindows()
    # det.save(img,"pimg_ou.png")
    # re = det.format_output(lang="zh")


if __name__ == "__main__":
    # pose_infer_demo()
    # det_infer_demo()
    # video_infer_demo()
    # hand_video_demo()
    # coco_det_demo
    # hand_det_demo()
    # face_det_demo()
    ocr_demo()
    # mmedu_demo()
    # demo()
    # basenn_demo()