from profil3r.app.modules.porn.pornhub import Pornhub
from profil3r.app.modules.porn.redtube import Redtube
from profil3r.app.modules.porn.xvideos import Xvideos

# Pornhub
def pornhub(self):
    self.result["pornhub"] = Pornhub(self.config, self.permutations_list).search()
    # print results
    self.print_results("pornhub")
    return self.result["pornhub"]

# Redtube
def redtube(self):
    self.result["redtube"] = Redtube(self.config, self.permutations_list).search()
    # print results
    self.print_results("redtube")
    return self.result["redtube"]

# XVideos
def xvideos(self):
    self.result["xvideos"] = Xvideos(self.config, self.permutations_list).search()
    # print results
    self.print_results("xvideos")
    return self.result["xvideos"]