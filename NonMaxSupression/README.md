Non-maxima suppression

    Args
    bboxes: [num_boxes,6] 
        -> Here, 6 channels are in order [x,y,x,y,box_confidence,class_mask]
        -> class_mask is a single channel output comprising class_id values. class_id -> [0, num(classes)-1]
    NOTE: The coordinates here are in the order of xyxy as opposed to xywh (in the rest of the code)

    score_threshold: threshold for box confidence score
    iou_threshold: threshold for IOU (Intersection-over-Union)

    Output
    best_boxes: [reduced_num_boxes,6]
    TODO


    Test Case 1: Basic functionality.
    Input:
    bboxes: [[10, 10, 50, 50, 0.9, 1], [15, 15, 55, 55, 0.8, 1]]
    score_threshold: 0.7
    iou_threshold: 0.5
    method: 'nms'
    Expected Output:
    [[10, 10, 50, 50, 0.9, 1]]

    Test Case 2: Multiple classes.
    Input:
    bboxes: [[10, 10, 50, 50, 0.9, 1], [15, 15, 55, 55, 0.8, 1], [100, 100, 150, 150, 0.95, 2], [105, 105, 155, 155, 0.85, 2]]
    score_threshold: 0.7
    iou_threshold: 0.5
    method: 'nms'
    Expected Output:
    [[10, 10, 50, 50, 0.9, 1], [100, 100, 150, 150, 0.95, 2]]