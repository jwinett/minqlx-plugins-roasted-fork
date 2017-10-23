import minqlx

PLAYER_KEY = "minqlx:players:{}"

country_code_anthems = {'AF': 'afghanistan', 'SO': 'somalia', 'JP': 'japan-youtube', 'RU': 'russia', 'VA': 'vaticancity', 'CG': 'republicofthecongo', 'GR': 'greece', 'NO': 'norway', 'BF': 'burkinafaso', 'KH': 'cambodia-youtube', 'CN': 'china', 'TV': 'tuvalu', 'ET': 'ethiopia', 'AW': 'aruba', 'AG': 'antiguaandbarbuda', 'CO': 'colombia', 'VN': 'vietnam', 'LU': 'luxembourg', 'NL': 'netherlands', 'SM': 'sanmarino-youtube', 'FJ': 'fiji', 'BE': 'belgium', 'FR': 'france', 'LK': 'srilanka', 'CR': 'costarica', 'FM': 'micronesia', 'KG': 'kyrgyzstan', 'PE': 'peru', 'ML': 'mali', 'CY': 'cyprus', 'SL': 'sierraleone', 'ZM': 'zambia', 'NP': 'nepal', 'LT': 'lithuania', 'HR': 'croatia', 'IL': 'israel', 'PH': 'philippines', 'GH': 'ghana', 'BN': 'brunei', 'CL': 'chile', 'SC': 'seychelles', 'KP': 'northkorea', 'MN': 'mongolia', 'BW': 'botswana', 'BI': 'burundi', 'KR': 'southkorea', 'MU': 'mauritius', 'BJ': 'benin', 'GD': 'grenada', 'PW': 'palau', 'GA': 'gabon', 'ZA': 'southafrica', 'MR': 'mauritania', 'BH': 'bahrain', 'SD': 'sudan', 'RS': 'serbia', 'XK': 'kosovo', 'GY': 'guyana', 'MD': 'moldova', 'ER': 'eritrea', 'GM': 'gambia', 'VE': 'venezuela', 'PK': 'pakistan', 'SE': 'sweden', 'AT': 'austria', 'TH': 'thailand', 'SN': 'senegal', 'DE': 'germany', 'MX': 'mexico', 'HT': 'haiti', 'TR': 'turkey', 'AL': 'albania', 'TL': 'easttimor', 'PG': 'papuanewguinea', 'BG': 'bulgaria', 'VU': 'vanuatu', 'AM': 'armenia', 'AD': 'andorra', 'SR': 'suriname', 'AZ': 'azerbaijan', 'KZ': 'kazakhstan', 'JO': 'jordan', 'DM': 'dominica', 'IT': 'italy', 'TD': 'chad', 'RW': 'rwanda', 'GT': 'guatemala', 'SG': 'singapore', 'EG': 'egypt', 'MH': 'marshallislands', 'KE': 'kenya', 'IQ': 'iraq', 'BR': 'brazil', 'KW': 'kuwait', 'DJ': 'djibouti', 'YE': 'yemen', 'MC': 'monaco', 'GB': 'unitedkingdom', 'BD': 'bangladesh', 'LA': 'laos', 'AE': 'unitedarabemirates', 'NI': 'nicaragua', 'ME': 'montenegro', 'US': 'unitedstatesofamerica', 'LC': 'stlucia', 'TN': 'tunisia', 'HU': 'hungary', 'PA': 'panama', 'MA': 'morocco', 'TT': 'trinidadandtobago', 'UZ': 'uzbekistan', 'LB': 'lebanon', 'CZ': 'czechrepublic', 'JM': 'jamaica', 'HN': 'honduras', 'IN': 'india-janaganamana', 'BY': 'belarus', 'UA': 'ukraine', 'PL': 'poland', 'SI': 'slovenia', 'LR': 'liberia', 'SZ': 'swaziland', 'MY': 'malaysia', 'CK': 'thecookislands', 'BA': 'bosniaandherzegovina', 'MG': 'madagascar', 'AU': 'australia', 'BS': 'thebahamas', 'MW': 'malawi', 'CA': 'canada', 'DK': 'denmark', 'MT': 'malta', 'WS': 'samoa', 'LI': 'liechtenstein', 'CV': 'capeverde', 'CI': 'theivorycoast', 'CH': 'switzerland', 'OM': 'oman', 'LY': 'libya', 'GE': 'georgia', 'BT': 'bhutan', 'NA': 'namibia', 'SV': 'elsalvador', 'EC': 'ecuador', 'LV': 'latvia', 'IR': 'iran', 'PY': 'paraguay', 'TO': 'tonga', 'NZ': 'newzealand', 'BB': 'barbados', 'CM': 'cameroon', 'SA': 'saudiarabia', 'CF': 'centralafricanrepublic', 'KM': 'comoros', 'BZ': 'belize', 'AR': 'argentina', 'AO': 'angola', 'RO': 'romania', 'NE': 'nigeria', 'MZ': 'mozambique', 'CU': 'cuba', 'PT': 'portugal', 'GN': 'guinea-bisssau', 'SK': 'slovakia', 'MV': 'themaldives', 'TZ': 'tanzania', 'TG': 'togo', 'DZ': 'algeria', 'UY': 'uruguay', 'TM': 'turkmenistan', 'ST': 'saotomeandprincipe-independenciatotal', 'PR': 'puertorico', 'MM': 'burma', 'QA': 'qatar', 'FI': 'finland', 'ID': 'indonesia', 'ES': 'spain', 'MK': 'macedonia', 'EE': 'estonia', 'BO': 'bolivia'}

SONGS = [
    ("Slayer - Angel of Death", "sound/allah/slayer-angel_of_death.ogg"),
    ("Nine Inch Nails - March of the Pigs", "sound/allah/march_of_the_pigs.ogg"),
    ("Quake 1 - Intro", "sound/allah/quake1_track2.ogg"),
    ("Deftones - Swerve City", "sound/allah/swerve_city.ogg"),
    ("Doom 1 - E2M2", "sound/allah/doom1_e2m2.ogg"),
    ("Megadeth - Escape Velocity", "sound/allah/megadeth-escape_velocity.ogg"),
    ("Deftones - Hole in the Earth", "sound/allah/deftones-hole_in_the_earth.ogg"),
    ("Megadeth - Duke Nukem theme", "sound/allah/duketheme.ogg"),
    ("Filter - Welcome to the Fold", "sound/allah/filter-welcome_to_the_fold.ogg"),
    ("Mastodon - The Motherload", "sound/allah/mastadon-the_motherload.ogg"),
    ("Megadeth - Hangar 18", "sound/allah/megadeth-hangar_18.ogg"),
    ("Meshuggah - Bleed", "sound/allah/meshuggah-bleed.ogg"),
    ("Nine Inch Nails - Burn", "sound/allah/nin-burn.ogg"),
    ("Death - Painkiller", "sound/allah/painkiller.ogg"),
    ("Nirvana - Negative Creep", "sound/allah/nirvana-negative_creep.ogg"),
    ("Primus - Wynonas Big Brown Beaver", "sound/allah/primus-wynonas_big_brown_beaver.ogg"),
    ("Rage Against the Machine - Bulls on Parade", "sound/allah/ratm-bulls_on_parade.ogg"),
    ("Tool - Bulls on Parade", "sound/allah/tool-intermission.ogg"),
    ("White Zombie - Thunder Kiss 65", "sound/allah/white_zombie-thunder_kiss_65.ogg"),
    ("Gojira - Stranded", "sound/allah/stranded.ogg"),
    ("Pantera - 5 Minutes Alone", "sound/allah/pantera-5minutes-alone.ogg"),
    ("Doom 2 - Map 1", "sound/allah/doom2_1.ogg"),
    ("Death - Crystal Mountain", "sound/allah/crystal_mountain.ogg"),
    ("Mastodon - Precious Stones", "sound/allah/mastodon-precious_stones.ogg"),
    ("Chemical Brothers - Block Rockin Beats", "sound/allah/block_rockin_beats.ogg"),
    ("Filter - You Walk Away", "sound/allah/filter-you_walk_away.ogg"),
    ("Doom 2 - runnin", "sound/allah/doom2_runnin.ogg"),
    ("Nirvana - Scentless Apprentice", "sound/allah/scentless_apprentice"),
    ("Meshuggah - Rational Gaze", "sound/allah/meshuggah-rational_gaze.ogg"),
    ("Doom 1 - E1M1", "sound/allah/doom1_e1m1.ogg"),
    ("Static-X - Shadow Zone", "sound/allah/shadow_zone.ogg"),
    ("Green Day - Longview", "sound/allah/longview.ogg"),
    ("Doom 2 - Intermission", "sound/allah/doom2_int.ogg"),
    ("Alice in Chains - Rooster", "sound/allah/alice-in-chains_rooster.ogg"),
    ("Aphex Twin - Come to Daddy", "sound/allah/aphex-twin-come_to_daddy.ogg"),
    ("Filter - Hey Man Nice Shot", "sound/allah/filter-hey_man_nice_shot.ogg"),
    ("Alexisonfire - Funeral", "sound/allah/alexis-funeral.ogg"),
    ("Animals as Leaders - Behaving Badly", "sound/allah/animals-behaving.ogg"),
    ("Animals as Leaders - Woven Web", "sound/allah/animals-web.ogg"),
    ("Aphex Twin - Wet Tip", "sound/allah/afx-wet_tip.ogg"),
    ("Aphex Twin - Phonatacid", "sound/allah/afx-phontacid.ogg"),
    ("Billy Talent - Devil in a Midnight Mass", "sound/allah/billy-devil.ogg"),
    ("Bjork - Army of Me", "sound/allah/bjork-army.ogg"),
    ("Bush - Machinehead", "sound/allah/bush-machine.ogg"),
    ("Angel Vivaldi - A Mercurian Summer", "sound/allah/angel-mercury.ogg"),
    ("Chemical Brothers - Setting Sun", "sound/allah/chemical-sun.ogg"),
    ("Rick Astley - Never Gonna Give you Up", "sound/allah/never_gonna_give_you_up.ogg")
]

class intermissionplus(minqlx.Plugin):

    def __init__(self):
        self.add_hook("game_end", self.handle_game_end)
        self.add_hook("stats", self.handle_stats)

        self.add_command("victorysong", self.cmd_victorysong, usage="<victorysong number option> - Type: !victorysongs for options", client_cmd_perm=0)
        self.add_command("victorysongs", self.cmd_victorysongs,  client_cmd_perm=0)

        self.winner = ""
        self.index = 0

    @minqlx.thread
    def cmd_victorysongs(self, player, msg, channel):
        for i, (song) in enumerate(SONGS):
            player.tell("^2{}: ^7{}".format(i, song[0]))
        player.tell("^2999: ^7Your Countries' Anthem")
        player.tell("^1Type: ^7!victorysong <song number> ^3to set your victorysong! :D")

    def cmd_victorysong(self, player, msg, channel):
        if len(msg) < 2:
            victorysong_number = self.db.get(PLAYER_KEY.format(player.steam_id) + ":victorysong")
            if victorysong_number: int(victorysong_number)
            if victorysong_number:
                if victorysong_number == 999:
                    victorysong_string = "Your Countries' Anthem"
                else:
                    victorysong_string = SONGS[victorysong_number][0]
                player.tell("^3Your current victorysong is: ^7{} - ^3Type: !victorysongs for list - !victorysong <song number> to change".format(victorysong_string))
            else:
                return minqlx.RET_USAGE
        else:
            try:
                arg = int(msg[1])
                if 0 <= arg <= len(SONGS) - 1 or arg == 999:
                    self.db.set(PLAYER_KEY.format(player.steam_id) + ":victorysong", arg)
                    victorysong_number = int(self.db[PLAYER_KEY.format(player.steam_id) + ":victorysong"])
                    if arg == 999:
                        victorysong_string = "Your Countries' Anthem"
                    else:
                        victorysong_string = SONGS[victorysong_number][0]
                    player.tell("^3Your victorysong has been set to: ^7{}!".format(victorysong_string))
                else:
                    raise ValueError
            except ValueError:
                player.tell("^1Invalid victorysong!")

    def handle_stats(self, stats):
        if stats['TYPE'] == "PLAYER_STATS":
            if stats['DATA']['QUIT'] == 0 and stats['DATA']['WARMUP'] == 0 and stats['DATA']['LOSE'] == 0:
                if int(stats['DATA']['STEAM_ID']) != 0:
                    self.winner = self.player(int(stats['DATA']['STEAM_ID']))
                else:
                    self.winner = "bot"

    @minqlx.delay(0.3)
    def handle_game_end(self, data):
        if not data["ABORTED"]:
            if self.winner != "bot":
                victorysong_number = int(self.db[PLAYER_KEY.format(self.winner.steam_id) + ":victorysong"])
                if victorysong_number:
                    if victorysong_number == 999:
                        if self.winner.country in country_code_anthems:
                            self.msg("^6Now Playing Country Anthem for {}^7: ^3{} - ^1 Please rise!".format(self.winner.name, country_code_anthems[self.winner.country]))
                            self.song_player("sound/anthems/{}.ogg".format(country_code_anthems[self.winner.country]))
                    else:
                        self.msg("^6Now Playing victorysong for {}^7: ^3{}".format(self.winner.name, SONGS[victorysong_number][0]))
                        self.song_player("{}".format(SONGS[victorysong_number][1]))
                else:
                    player.tell("^1You don't have a victory song set - ^3Type: !victorysongs for list - !victorysong <song number> to set")
                    if self.index == len(SONGS):
                        self.index = 0
                    self.song_player(SONGS[self.index][1])
                    self.index += 1
            else:
                self.song_player("sound/anthems/roboto.ogg")

        self.winner = ""

    def song_player(self, song):
        for p in self.players():
            if self.db.get_flag(p, "essentials:sounds_enabled", default=True):
                self.stop_music(p)
                self.play_sound(song, p)


