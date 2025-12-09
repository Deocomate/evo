import cv2
import mediapipe as mp

def khoi_tao_mediapipe():
    """Khởi tạo các module của MediaPipe"""
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    mp_styles = mp.solutions.drawing_styles
    
    # Cấu hình module Hands
    hands = mp_hands.Hands(
        static_image_mode=False,      # False để tối ưu cho video stream
        max_num_hands=2,              # Số lượng tay tối đa muốn nhận diện
        min_detection_confidence=0.5, # Độ tin cậy tối thiểu để phát hiện tay
        min_tracking_confidence=0.5   # Độ tin cậy tối thiểu để theo dõi tay
    )
    return hands, mp_draw, mp_styles, mp_hands

def xu_ly_khung_hinh(frame, hands_detector):
    """Xử lý ảnh đầu vào và trả về kết quả nhận diện"""
    # Lật ngược ảnh (hiệu ứng gương) để tự nhiên hơn khi soi cam
    frame = cv2.flip(frame, 1)
    
    # MediaPipe yêu cầu ảnh đầu vào là RGB, OpenCV đọc là BGR
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Thực hiện nhận diện
    results = hands_detector.process(frame_rgb)
    
    return frame, results

def ve_landmark(frame, results, mp_draw, mp_styles, mp_hands):
    """Vẽ các điểm mốc (landmark) lên khung hình"""
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )
    return frame

def main():
    cap = cv2.VideoCapture(0) # Mở webcam mặc định
    
    # 1. Khởi tạo
    hands_detector, mp_draw, mp_styles, mp_hands = khoi_tao_mediapipe()
    
    print("Đang chạy... Nhấn 'q' để thoát.")
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Không thể nhận khung hình từ camera.")
            break

        # 2. Xử lý khung hình
        frame, results = xu_ly_khung_hinh(frame, hands_detector)
        
        # 3. Vẽ landmark
        frame = ve_landmark(frame, results, mp_draw, mp_styles, mp_hands)
        
        # 4. Hiển thị
        cv2.imshow('Minh Long - MediaPipe Hands', frame)
        
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()