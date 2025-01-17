from profil3r.app.modules.music.soundcloud import Soundcloud
from profil3r.app.modules.music.spotify import Spotify
from profil3r.app.modules.music.smule import Smule

# Soundcloud
def soundcloud(self):
    self.result["soundcloud"] = Soundcloud(self.config, self.permutations_list).search()
    # print results
    self.print_results("soundcloud")
    return self.result["soundcloud"]

# Soundcloud
def spotify(self):
    self.result["spotify"] = Spotify(self.config, self.permutations_list).search()
    # print results
    self.print_results("spotify")
    return self.result["spotify"]

# Smule
def smule(self):
    self.result["smule"] = Smule(self.config, self.permutations_list).search()
    # print results
    self.print_results("smule")
    return self.result["smule"]