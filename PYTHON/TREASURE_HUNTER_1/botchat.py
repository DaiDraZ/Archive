# import random
# import time
# import keyboard

# # Định nghĩa một số thông số cơ bản cho trò chơi
# MAP_WIDTH = 10
# MAP_HEIGHT = 10

# # Danh sách các khu vực trong game
# locations = {
#     "village": {
#         "name": "Ngôi Làng Bị Nguyền Rủa",
#         "description": "Một ngôi làng nhỏ, u ám với những ngôi nhà hoang tàn.",
#         "items": ["sách cổ", "bùa chú"]
#     },
#     "forest": {
#         "name": "Khu Rừng Bí Ẩn",
#         "description": "Rừng sâu với những cây cổ thụ lớn và tiếng gió rít qua các cành cây.",
#         "items": ["lá thảo dược", "cây gậy"]
#     },
#     "haunted_house": {
#         "name": "Ngôi Nhà Bỏ Hoang",
#         "description": "Ngôi nhà có cửa sổ tối, lạnh lẽo và các tiếng động lạ.",
#         "items": ["mắt ma", "bánh thánh"]
#     },
# }

# # Định nghĩa các câu đố
# puzzles = {
#     "village": "Để vào ngôi nhà, bạn cần tìm chìa khóa trong sách cổ.",
#     "forest": "Cây gậy có thể giúp bạn xua đuổi các sinh vật kỳ lạ.",
#     "haunted_house": "Bánh thánh sẽ làm yếu đi sức mạnh của linh hồn trong ngôi nhà.",
# }

# # Trạng thái trò chơi
# player_location = "village"
# inventory = []
# health = 100

# # Hàm in bản đồ
# def print_map():
#     print(f"\nBạn hiện đang ở: {locations[player_location]['name']}")
#     print(locations[player_location]["description"])
#     print(f"Đồ vật bạn có: {', '.join(inventory) if inventory else 'Không có gì'}")
#     print(f"Sức khỏe: {health}%")

# # Hàm giải câu đố
# def solve_puzzle():
#     global health
#     if player_location == "village" and "sách cổ" in inventory:
#         print("Bạn giải mã câu đố và tìm được chìa khóa! Cửa ngôi nhà mở ra.")
#     elif player_location == "forest" and "cây gậy" in inventory:
#         print("Bạn sử dụng cây gậy để xua đuổi các sinh vật kỳ lạ trong rừng.")
#     elif player_location == "haunted_house" and "bánh thánh" in inventory:
#         print("Bạn sử dụng bánh thánh để làm yếu đi linh hồn và mở cửa ngôi nhà.")
#     else:
#         print(f"Câu đố: {puzzles[player_location]}")
#         health -= 10  # Mất một chút sức khỏe nếu không giải được câu đố

# # Hàm di chuyển
# def move():
#     global player_location
#     print("\nBạn có thể di chuyển đến các khu vực sau: village, forest, haunted_house.")
#     move_to = input("Nhập khu vực bạn muốn di chuyển: ").strip().lower()

#     if move_to in locations:
#         player_location = move_to
#         print(f"\nBạn di chuyển đến {locations[player_location]['name']}.")
#     else:
#         print("Khu vực không hợp lệ.")

# # Hàm kiểm tra kết thúc game
# def check_game_over():
#     if health <= 0:
#         print("Bạn đã chết. Game Over!")
#         return True
#     return False

# # Hàm khởi tạo trò chơi
# def start_game():
#     global health
#     print_map()

#     while True:
#         if check_game_over():
#             break

#         action = input("\nBạn muốn làm gì? (di chuyển: 'move', giải câu đố: 'solve', kiểm tra sức khỏe: 'health', thoát: 'quit'): ").strip().lower()
        
#         if action == "move":
#             move()
#         elif action == "solve":
#             solve_puzzle()
#         elif action == "health":
#             print(f"Sức khỏe của bạn: {health}%")
#         elif action == "quit":
#             print("Bạn đã thoát khỏi trò chơi.")
#             break
#         else:
#             print("Hành động không hợp lệ!")

#         print_map()
#         time.sleep(1)

# if __name__ == "__main__":
#     start_game()

import os
import time
import random
import keyboard

# Định nghĩa kích thước màn hình trò chơi
ROAD_WIDTH = 20
SCREEN_HEIGHT = 20

# Xe của người chơi
PLAYER_CAR = "A"

# Đường đua và xe
EMPTY = " "
OBSTACLE = "X"
road = [[EMPTY] * ROAD_WIDTH for _ in range(SCREEN_HEIGHT)]

# Vị trí ban đầu của người chơi
player_position = ROAD_WIDTH // 2
player_score = 0
game_over = False

def draw_screen():
    """Hiển thị màn hình."""
    buffer = "\n".join(
        "|" + "".join(road[y]) + "|" for y in range(SCREEN_HEIGHT)
    )
    stats = f"\nĐiểm số: {player_score}\n{'=' * (ROAD_WIDTH + 2)}"
    print(f"{buffer}{stats}", end="", flush=True)

def update_road():
    """Di chuyển chướng ngại vật xuống dưới."""
    global road

    # Tạo hàng mới ở trên cùng
    new_row = [EMPTY] * ROAD_WIDTH
    if random.random() < 0.3:  # 30% xác suất xuất hiện chướng ngại vật
        obstacle_position = random.randint(0, ROAD_WIDTH - 1)
        new_row[obstacle_position] = OBSTACLE

    # Thêm hàng mới vào trên cùng và xóa hàng cuối
    road.insert(0, new_row)
    road.pop()

def check_collision():
    """Kiểm tra va chạm giữa xe người chơi và chướng ngại vật."""
    global game_over

    if road[-1][player_position] == OBSTACLE:
        game_over = True

def move_player():
    """Di chuyển xe của người chơi."""
    global player_position

    if keyboard.is_pressed("left") and player_position > 0:
        player_position -= 1
    elif keyboard.is_pressed("right") and player_position < ROAD_WIDTH - 1:
        player_position += 1

def place_player():
    """Đặt xe của người chơi vào vị trí trên đường."""
    road[-1] = [EMPTY] * ROAD_WIDTH  # Làm sạch dòng cuối
    road[-1][player_position] = PLAYER_CAR  # Đặt xe người chơi

def game_loop():
    """Vòng lặp chính của trò chơi."""
    global player_score, game_over

    last_update_time = time.time()
    frame_delay = 0.1  # Tăng tốc độ khung hình (10 FPS)

    while not game_over:
        current_time = time.time()

        if current_time - last_update_time >= frame_delay:
            update_road()
            check_collision()
            if game_over:
                break

            move_player()
            place_player()
            draw_screen()

            player_score += 1
            last_update_time = current_time

    print("\nGAME OVER! Bạn đạt được:", player_score)

if __name__ == "__main__":
    try:
        print("Bắt đầu trò chơi... Nhấn 'q' để thoát!")
        time.sleep(1)

        while True:
            # Khởi tạo lại các biến toàn cục
            road = [[EMPTY] * ROAD_WIDTH for _ in range(SCREEN_HEIGHT)]
            player_position = ROAD_WIDTH // 2
            player_score = 0
            game_over = False

            # Xóa màn hình trước khi bắt đầu
            os.system('cls' if os.name == 'nt' else 'clear')

            # Chạy trò chơi
            game_loop()

            # Lựa chọn chơi lại hoặc thoát
            if input("\nNhấn 'Enter' để chơi lại hoặc 'q' để thoát: ").strip().lower() == 'q':
                break

    except KeyboardInterrupt:
        print("\nTrò chơi đã kết thúc.")


