from profil3r.app.modules.entertainment.dailymotion import Dailymotion
from profil3r.app.modules.entertainment.vimeo import Vimeo
from profil3r.app.modules.entertainment.deviantart import Deviantart

# Dailymotion
def dailymotion(self):
    self.result["dailymotion"] = Dailymotion(self.config, self.permutations_list).search() 
    # print results
    self.print_results("dailymotion")
    return self.result["dailymotion"]

# Vimeo
def vimeo(self):
    self.result["vimeo"] = Vimeo(self.config, self.permutations_list).search() 
    # print results
    self.print_results("vimeo")
    return self.result["vimeo"]

# DeviantArt
def deviantart(self):
    self.result["deviantart"] = Deviantart(self.config, self.permutations_list).search() 
    # print results
    self.print_results("deviantart")
    return self.result["deviantart"]