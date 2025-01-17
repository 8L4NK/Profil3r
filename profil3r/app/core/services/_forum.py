from profil3r.app.modules.forum.zeroxzerozerosec import Zeroxzerozerosec
from profil3r.app.modules.forum.jeuxvideo import Jeuxvideo
from profil3r.app.modules.forum.hackernews import Hackernews
from profil3r.app.modules.forum.crackedto import Crackedto
from profil3r.app.modules.forum.lesswrong import Lesswrong

# 0x00sec
def zeroxzerozerosec(self):
    self.result["0x00sec"] = Zeroxzerozerosec(self.config, self.permutations_list).search() 
    # print results
    self.print_results("0x00sec")
    return self.result["0x00sec"]

# jeuxvideo.com
def jeuxvideo(self):
    self.result["jeuxvideo.com"] = Jeuxvideo(self.config, self.permutations_list).search() 
    # print results
    self.print_results("jeuxvideo.com")
    return self.result["jeuxvideo.com"]

# Hackernews
def hackernews(self):
    self.result["hackernews"] = Hackernews(self.config, self.permutations_list).search() 
    # print results
    self.print_results("hackernews")
    return self.result["hackernews"]

# Cracked.to
def crackedto(self):
    self.result["crackedto"] = Crackedto(self.config, self.permutations_list).search() 
    # print results
    self.print_results("crackedto")
    return self.result["crackedto"]

# LessWrong
def lesswrong(self):
    self.result["lesswrong"] = Lesswrong(self.config, self.permutations_list).search() 
    # print results
    self.print_results("lesswrong")
    return self.result["lesswrong"]