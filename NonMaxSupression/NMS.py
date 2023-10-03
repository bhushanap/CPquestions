import numpy as np

def nms(bboxes, score_threshold, iou_threshold, sigma=0.3, method='nms'):
        classes = {}
        for bbox in bboxes:
            if bbox[4]<score_threshold:
                continue
            cls = bbox[5]
            if not cls in classes:
                classes[cls] = [bbox]
            else:
                classes[cls].append(bbox)

        for cls in classes:
            classes[cls] = np.array(classes[cls])
            classes[cls] = (classes[cls])[np.argsort((classes[cls])[:, 4])[::-1]]

        for cls in classes:
            arr = classes[cls]
            i=0
            j=1
            while True: 
                try:
                    arr[i]
                except IndexError:
                    break
                try:
                    arr[j]
                except IndexError:
                    i+=1
                    j=i+1
                    continue
                # print(arr[i],arr[j])
                if iou(arr[i],arr[j])<iou_threshold:
                    # print('delete')
                    arr = np.delete(arr, j, 0)
                    continue
                else:
                    j+=1
            classes[cls] = arr

        out = []
        for cls in classes:
            for box in classes[cls]:
                out.append(box)

        return np.array(out)

def iou(box1, box2):
  x1, y1, x2, y2 = box1[:4]
  x3, y3, x4, y4 = box1[:4]
  if x3>x2 or y3>y2:
    return 0
  else:
    i = (y2-y3)*(x3-x2)
    u = (y2-y1)*(x2-x1) + (y4-y3)*(x4-x3) - i
    return  i/u