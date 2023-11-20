# error
import pygame

pygame.init()

# 점수와 이미지 파일 이름을 저장하는 함수
def save_info(score, image_file):
    with open("info.txt", "w") as file:
        file.write(f"Score: {score}, Image: {image_file}")

# 점수와 이미지 파일 이름을 불러오는 함수
def load_info():
    try:
        with open("info.txt", "r") as file:
            data = file.read()
            score_part, image_part = data.split(", ")
            score = int(score_part.split(": ")[1])
            image_file = image_part.split(": ")[1]
            return score, image_file
    except FileNotFoundError:
        # 파일이 없을 경우 기본 점수 0과 기본 이미지로 설정
        return 0, '2R/images/1.png'

# 게임 시작 시 정보 불러오기
player_score, selected_image_file = load_info()

# 이미지 로드
selected_image = pygame.image.load(selected_image_file)


WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("SONOL")

# 폰트 설정
font = pygame.font.SysFont('arial', 24)
shop_font = pygame.font.SysFont('arial', 40)  # 'SHOP' 텍스트를 위한 폰트
button_font = pygame.font.SysFont('arial', 40)  # 버튼 텍스트를 위한 폰트

# 버튼 색상
button_king_color = (255, 215, 0)
button_angel_color = (173, 216, 230)
button_leaf_color = (0, 255, 0)
button_Santa_color = (255, 0, 0)
buy_button_color = (128, 128, 128)  # BUY 버튼 색상


# 이미지 로드 및 변환
king_image = pygame.image.load('3R/images/kingPacman.png')
angel_image = pygame.image.load('3R/images/angelPacman.png')
leaf_image = pygame.image.load('3R/images/leafPacman.png')
king_image = pygame.transform.scale(king_image, (300, 300))
angel_image = pygame.transform.scale(angel_image, (300, 300))
leaf_image = pygame.transform.scale(leaf_image, (300, 300))

selected_image = None
buy_button = None

# 버튼 생성
button_king = pygame.draw.rect(screen, button_king_color, (70, 215, 300, 70))
button_angel = pygame.draw.rect(screen, button_angel_color, (70, 475, 300, 70))
button_leaf = pygame.draw.rect(screen, button_leaf_color, (70, 345, 300, 70))
button_Santa = pygame.draw.rect(screen, button_Santa_color, (70, 605, 300, 70))

run = True
while run:
    # 화면 지우기
    screen.fill((0, 0, 0))  # 화면을 검은색으로 채웁니다.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_king.collidepoint(mouse_pos):
                selected_image = king_image
            elif button_angel.collidepoint(mouse_pos):
                selected_image = angel_image
            elif button_leaf.collidepoint(mouse_pos):
                selected_image = leaf_image
            elif button_Santa.collidepoint(mouse_pos):
                selected_image = king_image

            if selected_image and buy_button and buy_button.collidepoint(mouse_pos):
                # BUY 버튼 클릭 시
                save_info(player_score, selected_image_file)


        elif button_king.collidepoint(mouse_pos):
            selected_image = king_image
        elif button_angel.collidepoint(mouse_pos):
            selected_image = angel_image
        elif button_leaf.collidepoint(mouse_pos):
            selected_image = leaf_image

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if selected_image and buy_button.collidepoint(mouse_pos):
                # 'BUY' 버튼 클릭 시 수행할 동작
                # BUY 버튼 클릭 시점 또는 게임 종료 시점에 호출
                save_info(player_score, selected_image_file)

            elif button_king.collidepoint(mouse_pos):
                selected_image = king_image
            elif button_angel.collidepoint(mouse_pos):
                selected_image = angel_image
            elif button_leaf.collidepoint(mouse_pos):
                selected_image = leaf_image
            elif button_Santa.collidepoint(mouse_pos):
                selected_image = king_image

    score_text = font.render(f'Score: {player_score}', True, (255, 255, 255))

    if selected_image:
        image_rect = screen.blit(selected_image, (500, 300))
         # BUY 버튼 설정
        buy_button = pygame.draw.rect(screen, buy_button_color, (520, 675, 250, 50))
        buy_text = button_font.render('BUY', True, (255, 255, 255))
        screen.blit(buy_text, (buy_button.x + (buy_button.width - buy_text.get_width()) // 2, buy_button.y + (buy_button.height - buy_text.get_height()) // 2))


    # 텍스트 렌더링 및 화면에 표시
    king_text = font.render('King', True, (0, 0, 0))
    angel_text = font.render('Angel', True, (0, 0, 0))
    leaf_text = font.render('Leaf', True, (0, 0, 0))
    Santa_text = font.render('Santa', True, (0, 0, 0))

    screen.blit(king_text, (70 + 150 - king_text.get_width() // 2, 215 + 35 - king_text.get_height() // 2))
    '''
    70 : 버튼의 시작점, 150 : 버튼의 크기의 절반, -king_text.get_width() : 폰트 크기의 절반
    '''
    screen.blit(angel_text, (70 + 150 - angel_text.get_width() // 2, 475 + 35 - angel_text.get_height() // 2))
    screen.blit(leaf_text, (70 + 150 - leaf_text.get_width() // 2, 345 + 35 - leaf_text.get_height() // 2))
    screen.blit(Santa_text, (70 + 150 - Santa_text.get_width() // 2, 605 + 35 - Santa_text.get_height() // 2))
    screen.blit(score_text, (10, 10))  # 화면의 원하는 위치에 텍스트 표시

    shop_text = shop_font.render('SHOP', True, (255, 255, 255))
    shop_text_rect = shop_text.get_rect(center=(WIDTH // 2, 50))
    pygame.draw.rect(screen, (128, 128, 128), shop_text_rect.inflate(20, 20))  # 텍스트 주위에 테두리 추가
    screen.blit(shop_text, shop_text_rect)

    if event.type == pygame.MOUSEBUTTONDOWN and buy_button.collidepoint(event.pos):
        # 여기서 player_score 갱신 및 selected_image_file 업데이트
        save_info(player_score, selected_image_file)  # 새로운 점수와 이미지 파일 저장

    pygame.display.update()

pygame.quit()
