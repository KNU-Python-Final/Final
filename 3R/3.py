import pygame

pygame.init()

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
king_image_path = '3R/images/kingPacman.png'
angel_image_path = '3R/images/angelPacman.png'
leaf_image_path = '3R/images/leafPacman.png'
heartking_image_path = '3R/images/heartking_image.png'
heartangel_image_path = '3R/images/heartangel_image.png'
heartleaf_image_path = '3R/images/heartleaf_image.png'
exit_image_path = '3R/images/exit.png'


king_image = pygame.transform.scale(pygame.image.load(king_image_path), (300, 300))
angel_image = pygame.transform.scale(pygame.image.load(angel_image_path), (300, 300))
leaf_image = pygame.transform.scale(pygame.image.load(leaf_image_path), (300, 300))
heartking_image = pygame.transform.scale(pygame.image.load(heartking_image_path), (300, 300))
heartangel_image = pygame.transform.scale(pygame.image.load(heartangel_image_path), (300, 300))
heartleaf_image = pygame.transform.scale(pygame.image.load(heartleaf_image_path), (300, 300))
exit_img = pygame.transform.scale(pygame.image.load(exit_image_path), (40, 40))

selected_image = None
buy_button = None


run = True
while run:
    # 화면 지우기
    screen.fill((0, 0, 0))  # 화면을 검은색으로 채웁니다.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if selected_image and buy_button.collidepoint(mouse_pos):
                # 'BUY' 버튼 클릭 시 수행할 동작
                pass
            elif button_king.collidepoint(mouse_pos):
                selected_image = king_image
                selected_image_type = 'king'
            elif button_angel.collidepoint(mouse_pos):
                selected_image = angel_image
            elif button_leaf.collidepoint(mouse_pos):
                selected_image = leaf_image
            elif button_Santa.collidepoint(mouse_pos):
                selected_image = king_image
            elif button_heart_version.collidepoint(mouse_pos):
                if selected_image == king_image:
                    selected_image = heartking_image
                elif selected_image == heartking_image:
                    selected_image = king_image
                if selected_image == angel_image:
                    selected_image = heartangel_image
                elif selected_image == heartangel_image:
                    selected_image == angel_image
                if selected_image == leaf_image:
                    selected_image = heartleaf_image
                elif selected_image == heartleaf_image:
                    selected_image = leaf_image
            elif restart_button.collidepoint(mouse_pos):
                run = False
            elif exit_button.collidepoint(mouse_pos):
                run = False

    if selected_image:
        image_rect = screen.blit(selected_image, (500, 300))
         # BUY 버튼 설정
        buy_button = pygame.draw.rect(screen, buy_button_color, (520, 675, 250, 50))
        buy_text = button_font.render('BUY', True, (255, 255, 255))
        screen.blit(buy_text, (buy_button.x + (buy_button.width - buy_text.get_width()) // 2, buy_button.y + (buy_button.height - buy_text.get_height()) // 2))


    # 버튼 생성
    button_king = pygame.draw.rect(screen, button_king_color, (70, 215, 300, 70))
    button_angel = pygame.draw.rect(screen, button_angel_color, (70, 475, 300, 70))
    button_leaf = pygame.draw.rect(screen, button_leaf_color, (70, 345, 300, 70))
    button_Santa = pygame.draw.rect(screen, button_Santa_color, (70, 605, 300, 70))
    button_heart_version = pygame.draw.rect(screen, button_king_color, (550, 250, 30, 30))
    exit_button = pygame.draw.rect(screen, button_Santa_color, (860, 910, 40, 40))
    click_exit_button = pygame.draw.rect(screen, button_Santa_color, (860, 910, 40, 40))
    restart_button = pygame.draw.rect(screen, button_Santa_color, (820, 910, 40, 40))

    # 텍스트 렌더링 및 화면에 표시
    king_text = font.render('King', True, (0, 0, 0))
    angel_text = font.render('Angel', True, (0, 0, 0))
    leaf_text = font.render('Leaf', True, (0, 0, 0))
    Santa_text = font.render('Santa', True, (0, 0, 0))

    screen.blit(king_text, (70 + 150 - king_text.get_width() // 2, 215 + 35 - king_text.get_height() // 2))  # x, y 좌표
    screen.blit(angel_text, (70 + 150 - angel_text.get_width() // 2, 475 + 35 - angel_text.get_height() // 2))
    screen.blit(leaf_text, (70 + 150 - leaf_text.get_width() // 2, 345 + 35 - leaf_text.get_height() // 2))
    screen.blit(Santa_text, (70 + 150 - Santa_text.get_width() // 2, 605 + 35 - Santa_text.get_height() // 2))

    shop_text = shop_font.render('SHOP', True, (255, 255, 255))
    shop_text_rect = shop_text.get_rect(center=(WIDTH // 2, 50))
    pygame.draw.rect(screen, (128, 128, 128), shop_text_rect.inflate(20, 20))  # 텍스트 주위에 테두리 추가
    screen.blit(shop_text, shop_text_rect)

    screen.blit(exit_img, exit_button.topleft)
    pygame.display.update()

pygame.quit()