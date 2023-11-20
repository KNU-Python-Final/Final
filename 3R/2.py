import pygame

pygame.init()

def save_info(score, image_file):
    with open("info.txt", "w") as file: # info.txt 파일을 "w"(쓰기모드)로 열기
        file.write(f"Score: {score}, Image: {image_file}") # 문자열을 file에 쓰기

def load_info():
    try: # 이미지가 없을 때 (예외의 상황) 를 위한 코드
        with open("info.txt", "r") as file: # info.txt 파일을 "r"(읽기모드)로 열기
            data = file.read() # 파일의 내용을 문자열로 읽어 변수에 지정
            score_part, image_part = data.split(", ") # ", " 를 기준으로 데이터 나누기
            score = int(score_part.split(": ")[1]) # 두번째 요소를 정수로 반환하여 변수에 지정
            image_file = image_part.split(": ")[1] # 두번째 요소를 반환하여 변수에 지정
            return score, image_file # score, image_flie 반환
    except FileNotFoundError: # 예외 상황시
        return 0, '2R/images/1.png' # score = 0, image_file = 기본 이미지 로 변경

player_score, selected_image_file = load_info()

# 초기 설정 및 이미지 로드
WIDTH, HEIGHT = 900, 950
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # 창의크기 설정
pygame.display.set_caption("3round") # 제목 설정

font = pygame.font.SysFont('arial', 24)
shop_font = pygame.font.SysFont('arial', 40)
button_font = pygame.font.SysFont('arial', 40)

button_colors = [(255, 215, 0), (173, 216, 230), (0, 255, 0), (255, 0, 0), (128, 128, 128)] # 버튼의 색상(RGB) 지정

# 이미지 경로 지정
king_image_path = '3R/images/kingPacman.png'
angel_image_path = '3R/images/angelPacman.png'
leaf_image_path = '3R/images/leafPacman.png'

# 이미지 크기 조정
king_image = pygame.transform.scale(pygame.image.load(king_image_path), (300, 300))
angel_image = pygame.transform.scale(pygame.image.load(angel_image_path), (300, 300))
leaf_image = pygame.transform.scale(pygame.image.load(leaf_image_path), (300, 300))

selected_image = None
buy_button = None

run = True
while run:
    screen.fill((0, 0, 0)) # 백그라운드 색상 : 검은색

    # 버튼 4개 그리기
    button_king = pygame.draw.rect(screen, button_colors[0], (70, 215, 300, 70)) # x좌표, y좌표, 너비, 높이
    button_angel = pygame.draw.rect(screen, button_colors[1], (70, 475, 300, 70))
    button_leaf = pygame.draw.rect(screen, button_colors[2], (70, 345, 300, 70))
    button_Santa = pygame.draw.rect(screen, button_colors[3], (70, 605, 300, 70))

    for event in pygame.event.get(): # 이벤트 순회
        if event.type == pygame.QUIT:
            run = False # 창 끄기
        if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 버튼을 클릭했을 때
            mouse_pos = event.pos # 클릭한 위치를 변수에 지정
            if button_king.collidepoint(mouse_pos): # button_king의 좌표 안에서 마우스 클릭 했다면
                selected_image = king_image # 이미지 업데이트
                selected_image_file = king_image_path  # 이미지 파일 경로 업데이트
            elif button_angel.collidepoint(mouse_pos):
                selected_image = angel_image 
                selected_image_file = angel_image_path
            elif button_leaf.collidepoint(mouse_pos):
                selected_image = leaf_image
                selected_image_file = leaf_image_path
            elif button_Santa.collidepoint(mouse_pos):
                selected_image = king_image
                selected_image_file = king_image_path  # 예시로 동일한 이미지 경로 사용
            if buy_button and buy_button.collidepoint(mouse_pos):
                save_info(player_score, selected_image_file)

    if selected_image: # 이미지가 할당 되었는지 확인
        screen.blit(selected_image, (500, 300)) # 500, 300에 지정된 이미지 그리기
        buy_button = pygame.draw.rect(screen, button_colors[4], (520, 675, 250, 50)) # (520, 675)에 250x50 크기의 버튼 생성
        buy_text = button_font.render('BUY', True, (255, 255, 255)) # 텍스트 생성
        # buy_button 중앙에 buy_text 배치
        screen.blit(buy_text, (buy_button.x + (buy_button.width - buy_text.get_width()) // 2, buy_button.y + (buy_button.height - buy_text.get_height()) // 2))

    score_text = font.render(f'Score: {player_score}', True, (255, 255, 255)) # 텍스트 렌더링
    screen.blit(score_text, (10, 10)) # 렌더링된 텍스트를 화면에 표시

    king_text = font.render('King', True, (0, 0, 0)) # king_text 렌더링
    angel_text = font.render('Angel', True, (0, 0, 0)) # angel_text 렌더링
    leaf_text = font.render('Leaf', True, (0, 0, 0)) # leaf_text 렌더링
    Santa_text = font.render('Santa', True, (0, 0, 0)) # Santo_text 렌더링

    button_texts = [king_text, angel_text, leaf_text, Santa_text] # 
    button_positions = [(70, 215), (70, 475), (70, 345), (70, 605)] # 버튼의 위치 지정
    # button_texts, button_position을 결합하여 새로운 튜플 생성 >> text 와 text의 좌표를 생성
    for text, (x, y) in zip(button_texts, button_positions):
        screen.blit(text, (x + 150 - text.get_width() // 2, y + 35 - text.get_height() // 2)) # 텍스트를 버튼의 중앙에 오도록 배치

    shop_text = shop_font.render('SHOP', True, (255, 255, 255)) # shop 렌더링
    shop_text_rect = shop_text.get_rect(center=(WIDTH // 2, 50)) # shop rect 렌더링
    pygame.draw.rect(screen, (128, 128, 128), shop_text_rect.inflate(20, 20)) # inflate = 사각형을 텍스트 영역보다 20 픽셀씩 크기 생성
    screen.blit(shop_text, shop_text_rect) # 렌더링된 텍스트를 화면에 표시

    pygame.display.update()

pygame.quit()
