from profil3r.app.modules.tchat.skype import Skype

# Skype
def skype(self):
    self.result["skype"] = Skype(self.config, self.permutations_list).search() 
    # print results
    self.print_results("skype")
    return self.result["skype"]