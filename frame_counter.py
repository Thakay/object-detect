# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo that runs object detection on camera frames using OpenCV.

TEST_DATA=../all_models

Run face detection model:
python3 detect.py \
  --model ${TEST_DATA}/mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite

Run coco model:
python3 detect.py \
  --model ${TEST_DATA}/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
  --labels ${TEST_DATA}/coco_labels.txt

"""
import argparse
import cv2
import os
import time
import pprint

def main():
    default_model_dir = '../all_models'
    default_model = 'mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite'
    default_labels = 'coco_labels.txt'
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='.tflite model path',
                        default=os.path.join(default_model_dir,default_model))
    parser.add_argument('--labels', help='label file path',
                        default=os.path.join(default_model_dir, default_labels))
    parser.add_argument('--top_k', type=int, default=8,
                        help='number of categories with highest score to display')
    parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 0)
    parser.add_argument('--threshold', type=float, default=0.1,
                        help='classifier score threshold')
    parser.add_argument('--file', default='daylow.mp4',
                        help='filename')
    args = parser.parse_args()

    print('Loading {} with {} labels.'.format(args.model, args.labels))
    vidname = args.file
    video = cv2.VideoCapture(vidname)
    #cap = cv2.VideoCapture(args.camera_idx)
    imW = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    imH = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    row_size = 20  # pixels
    left_margin = 24  # pixels
    text_color = (0, 0, 255)  # red
    font_size = 1
    font_thickness = 1
    fps_avg_frame_count = 10
    # Variables to calculate FPS
    counter, fps = 0, 0
    start_time = time.time()
    data = []
    checkname = "test"
    vidname = args.file.split('.')[0]
    if not os.path.exists(f'./res/{vidname}'):
      os.mkdir(f'./res/{vidname}')
    scale_percent = 60 # percent of original size
    width_ = int(video.get(3) * scale_percent / 100)
    height_ = int(video.get(4) * scale_percent / 100)
    frameSize = (width_,height_)
    
    fps_rate = 20
    out = cv2.VideoWriter(f'{vidname}_{frameSize}_{fps_rate}fps.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps_rate , frameSize)
    while video.isOpened():
        
        ret, frame = video.read()
        if not ret:
            break
        cv2_im = frame
        
        counter += 1
        # Calculate the FPS
        if counter % fps_avg_frame_count == 0:
          end_time = time.time()
          fps = fps_avg_frame_count / (end_time - start_time)
          start_time = time.time()
                
        
            
        filename  = f'./res/{vidname}/frame{counter}.jpg'

        scale_percent = 60 # percent of original size
        width_ = int(cv2_im.shape[1] * scale_percent / 100)
        height_ = int(cv2_im.shape[0] * scale_percent / 100)
        dim = (width_, height_)
        resized = cv2.resize(cv2_im, dim, interpolation = cv2.INTER_AREA)

        # out.write(resized)
        cv2.imwrite(filename, cv2_im)
         
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # with open(f'./res/{checkname}{vidname}/res.txt','w') as f:
    #   f.write(pprint.pformat(data))
    
    print(cv2_im.shape)
    print(counter)
    # pprint.pprint(data)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()