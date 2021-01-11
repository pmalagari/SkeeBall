# initial_main.py

import pygame as pg
import os

# initialize pg
pg.init()


TITLE = "Skee Ball!"
WIDTH = 1200
HEIGHT = 750
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Skee Ball Game")

GAME_OVER = pg.transform.scale(pg.image.load(os.path.join("images","game_over.png")), (WIDTH,HEIGHT))
GAME_START = pg.transform.scale(pg.image.load(os.path.join("images","game_start.jpg")), (WIDTH,HEIGHT))

def main():
    run = True
    Ball_Rolled = 0
    Ball_Remain = 9
    Score = 0
    main_font = pg.font.SysFont("commicsans", 50)
 
    def redraw_start_game_window():
        # Clear window
        SCREEN.fill(BLACK)

        # Set background
        SCREEN.blit(GAME_START, (0,0))

        # Update display
        pg.display.update()
    
    def redraw_ingame_window():
        # Clear window
        SCREEN.fill(BLACK)

        # Draw Text
        Ball_Rolled_label = main_font.render(f"Balls Rolled: {Ball_Rolled}", 1, (RED))
        Ball_Remain_label = main_font.render(f"Balls Remaining: {Ball_Remain}", 1, RED)
        Score_label = main_font.render(f"Score: {Score}", 1, GREEN)

        # Text location within window
        SCREEN.blit(Ball_Rolled_label, (10,10))
        SCREEN.blit(Ball_Remain_label, (10,60))
        SCREEN.blit(Score_label, (10, 110))

        # Update display
        pg.display.update()
    
    def redraw_final_score_window():
        # Clear window
        SCREEN.fill(BLACK)

        # Set background
        SCREEN.blit(GAME_OVER, (0,0))

        # Draw Text
        Final_Score_label = main_font.render(f"Final Score: {Score}", 1, GREEN)
        Restart_label = main_font.render("Press Enter to play again", 1, WHITE)
        Quit_label = main_font.render("Press Q or close window to exit", 1, WHITE)

        # Text location within window
        SCREEN.blit(Final_Score_label, ((WIDTH/2)-(Final_Score_label.get_width()/2), 50))
        SCREEN.blit(Restart_label, ((WIDTH/2)-(Restart_label.get_width()/2), 80 + Final_Score_label.get_height()))
        SCREEN.blit(Quit_label, ((WIDTH/2)-(Quit_label.get_width()/2), 80 + 2 * Final_Score_label.get_height()))

        # Update display
        pg.display.update()


    while run:

        redraw_start_game_window()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
#                    playing = True
                 
                    while run:
                        redraw_ingame_window()

                        for event in pg.event.get():
                            # if window X is clicked set run=False.  This will break the current while loop.
                            if event.type == pg.QUIT:
                                run = False
                            
                            # Look for key presses
                            if event.type == pg.KEYDOWN:
                                
                                # End game if the 'q' key is pressed
                                if event.key == pg.K_q:
                                    run = False
                                
                                # Increase score by 10 is key '1' is pressed
                                if event.key == pg.K_1:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 10

                                # Increase score by 20 is key '2' is pressed
                                if event.key == pg.K_2:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 20

                                # Increase score by 30 is key '3' is pressed
                                if event.key == pg.K_3:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 30

                                # Increase score by 40 is key '4' is pressed
                                if event.key == pg.K_4:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 40

                                # Increase score by 50 is key '5' is pressed
                                if event.key == pg.K_5:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 50

                                # Increase score by 100 is key '6' is pressed
                                if event.key == pg.K_6:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 100

                                # Increase score by 100 is key '7' is pressed
                                if event.key == pg.K_7:
                                    Ball_Rolled = Ball_Rolled + 1
                                    Ball_Remain = Ball_Remain - 1
                                    Score = Score + 100
                            
                            # End game afer 9 balls have been rolled
                            if Ball_Rolled == 9:
#                                end = True
                                while run:
                                    redraw_final_score_window()
                                    for event in pg.event.get():
                                        # if window X is clicked set run=False.  This will break the current while loop.
                                        if event.type == pg.QUIT:
                                            run = False
                                        if event.type == pg.KEYDOWN:
                                            # End game if the 'q' key is pressed
                                            if event.key == pg.K_q:
                                                run = False
                                            # Restart game if the 'return' key is pressed
                                            if event.key == pg.K_RETURN:
                                                main()
                        
main()
pg.quit()