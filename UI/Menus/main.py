import sys

from Backend.RankingDAO import RankingsDAO
from Config.window_config import *
from app import Game

from UI.Text import Text
from UI.SongCard import SongCard

from Controllers.Audio import GeneralSFX

import cv2


class Main:
    def __init__(self, camera, player, asset_loader):
        self.asset_loader = asset_loader

        self.current_video = None

        self.camera = camera
        self.player = player

        self.title_text = None

        self.song_cards = [
            SongCard(
                position=(50, 150),
                song_name="I Want It That Way",
                creator="Backstreet Boys",
                album_image_path="Songs/I Want It That Way/image.jpeg",
                songs_fps=30,
            ),
            SongCard(
                position=(50, 300),
                song_name="Numb",
                creator="Linking Park",
                album_image_path="Songs/Numb/image.jpeg",
                songs_fps=30,
            ),
            SongCard(
                position=(50, 450),
                song_name="Vagalumes",
                creator="Pollo",
                album_image_path="Songs/Vagalumes/image.jpeg",
                songs_fps=30,
            ),
        ]

        self.frame_interval = 1
        self.last_frame = None
        self.frame_counter = 0

        self.rankings_dao = RankingsDAO()
        self.rankings_title = Text(
            msg="Rankings:",
            position=(WIDTH - 50 - int(WIDTH * 0.3), 300),
            color=WHITE,
            font_size=30,
            centered=False
        )
        self.rankings_texts = []
        self.player_ranking_text = None

    def run(self):
        first_song_name = self.song_cards[0].song_name
        pygame.mixer.music.load(f'Songs/{first_song_name}/song.mp3')
        pygame.mixer.music.play(loops=-1, start=0)

        self.current_video = self.asset_loader.assets[f'{first_song_name}']

        self.title_text = Text(msg=f"Bem vindo! {self.player[1] if self.player is not None else 'Desconhecido'}",
                               position=(50, 50), color=WHITE, font_size=40,
                               centered=False)
        self.update_rankings_display(first_song_name)

        while True:
            CLOCK.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for song in self.song_cards:
                    response = song.handle_event(event)
                    match response:
                        case 'Go to game':
                            return song
                        case 'Update UI elements':
                            self.frame_interval = FPS / song.songs_fps
                            self.frame_counter = 0
                            self.current_video = self.asset_loader.assets[song.song_name]
                            self.current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                            GeneralSFX.play_song(song_name=song.song_name)
                            self.update_rankings_display(song.song_name)

            self.camera.internal_surface.fill(BLACK)

            self.title_text.draw(self.camera.internal_surface)

            for song in self.song_cards:
                song.draw(self.camera.internal_surface)

            self.display_video()

            self.rankings_title.draw(self.camera.internal_surface)
            for ranking_text in self.rankings_texts:
                ranking_text.draw(self.camera.internal_surface)
            if self.player_ranking_text:
                self.player_ranking_text.draw(self.camera.internal_surface)

            Game.blit_screen(self.camera)
            pygame.display.flip()

    def display_video(self):
        if self.frame_counter % self.frame_interval == 0:

            ret, frame = self.current_video.read()

            if not ret:
                self.current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = self.current_video.read()

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface = pygame.transform.scale(frame_surface, (int(WIDTH * 0.3), 216))

                self.last_frame = frame_surface

                self.camera.internal_surface.blit(frame_surface, (WIDTH - 50 - int(WIDTH * 0.3), 50))
        else:
            self.camera.internal_surface.blit(self.last_frame, (WIDTH - 50 - int(WIDTH * 0.3), 50))

        self.frame_counter += 1.0

    def update_rankings_display(self, song_name):
        top_rankings = self.rankings_dao.get_top_rankings_by_music(song_name, 5)

        self.rankings_texts.clear()

        start_y = 340
        for i, (_, nickname, score) in enumerate(top_rankings, 1):
            ranking_text = Text(
                msg=f"{i}. {nickname} - {round(score)}",
                position=(WIDTH - 50 - int(WIDTH * 0.3), start_y + (i * 30)),
                color=WHITE,
                font_size=25,
                centered=False
            )
            self.rankings_texts.append(ranking_text)

        if self.player:
            all_rankings = self.rankings_dao.get_rankings_by_music(song_name)
            player_rank = None
            player_score = None

            for i, (_, nickname, score) in enumerate(all_rankings, 1):
                if nickname == self.player[1]:
                    player_rank = i
                    player_score = round(score)
                    break

            self.player_ranking_text = Text(
                msg=f"Seu ranking: ",
                position=(WIDTH - 50 - int(WIDTH * 0.3), HEIGHT - 50),
                color=YELLOW,
                font_size=20,
                centered=False
            )

            if player_rank:
                self.player_ranking_text.msg += f'{player_rank}. {self.player[1]} - {player_score}'
            else:
                self.player_ranking_text.msg += 'Não rankeado'