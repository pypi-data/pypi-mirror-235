import os


class Config:
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    #CONFIG = f"{ROOT_DIR}\\configs\\config.cfg" 
    def __init__(self) -> None:

        self.config = f"{Config.ROOT_DIR}\\configs\\config.cfg" 
        self.oodle_path = ""
        self.tag_xml_template_path = "D:\\HaloInfiniteStuft\\Extracted\\UnPacked\\s4\\TagXml\\2023-08-11\\"
        #BASE_UNPACKED_PATH = "D:\\HaloInfiniteStuft\\Extracted\\UnPacked\\winter_update\\"
        self.base_unpacked_path = "D:\\HaloInfiniteStuft\\Extracted\\UnPacked\\emulate\\E\\"
        self.base_unpacked_path_campaign = "D:\\HaloInfiniteStuft\\Extracted\\UnPacked\\campaign\\"
        # BASE_UNPACKED_PATH = BASE_UNPACKED_PATH_CAMPAIGN
        self.model_export_path = "D:\\HaloInfiniteStuft\\Extracted\\Converted\\RE_OtherGames\\HI\\models\\"
        self.infos_path = 'C:\\Users\\Jorge\\Downloads\\Mover\\infos\\'
        self.export_json = 'J:\\Games\\Halo Infinite Stuf\\Extracted\\HI\\json\\'
        self.export_shaders = 'J:\\Games\\Halo Infinite Stuf\\Extracted\\shaderdis\\'
        self.spartan_style_path = "J:\\Games\\Halo Infinite Stuf\\Extracted\\UnPacked\\season2\\__chore\\gen__\\objects\\characters\\spartan_armor\\coatings\\"
        self.web_download_data = "J:\\Games\\Halo Infinite Stuf\\Web-Json\\"
        self.ue5_project_imported_pc_path = "H:\\UE4\\Unreal_Projects\\HaloInfinities " \
                                    "5.0\\Content\\__chore\\gen__\\pc__\\"
        self.deploy_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Halo Infinite\\deploy\\"
        self.deploy_path_campaign = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Halo Infinite\\deploy\\"
        self.exported_texture_path = "J:\\Games\\Halo Infinite Stuf\\Extracted\\Converted\\Textures\\TGA\\pc__\\"
        self.exported_texture_path_base = "J:\\Games\\Halo Infinite Stuf\\Extracted\\Converted\\Textures\\"

        self.verbose = True
    
    @classmethod
    def get_instance(cls):
        """Obtiene la instancia del singleton"""
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance
    
    def LoadConfig():
        path = Config.get_instance().config
        paths = {}

        with open(path,"r") as file:
            for line in file:
                entry = line.split('=')
                paths[entry[0].strip()] = entry[1].strip()
                if entry[0].strip() == "CONFIG":
                    Config.get_instance().config = entry[1].strip()
                elif entry[0].strip() == "DEPLOY_PATH":
                    Config.get_instance().deploy_path = entry[1].strip()
                elif entry[0].strip() == "DEPLOY_PATH_CAMPAIGN":
                    Config.get_instance().deploy_path_campaign = entry[1].strip()
                elif entry[0].strip() == "OODLE_PATH":
                    Config.get_instance().oodle_path = entry[1].strip()
                elif entry[0].strip() == "TAG_XML_TEMPLATE_PATH":
                    Config.get_instance().tag_xml_template_path = entry[1].strip()
        return paths
        
        
    def SaveConfEntry(key:str, value):
            update_val = Config.LoadConfig()
            update_val[key] = value
            with open(Config.get_instance().config, 'w') as f:
                for key in update_val.keys():
                    f.write(f"{key} = {update_val[key]}\n")

if not os.path.isfile(f"{Config.ROOT_DIR}\\configs\\config.cfg" ):
    with open(f"{Config.get_instance().config}" ,"xt") as file:
        file.write(f"ROOT_DIR = {Config.ROOT_DIR}\n")
        file.write(f"CONFIG = { Config.get_instance().config}\n")
        file.write(f"DEPLOY_PATH = {Config.get_instance().deploy_path}\n")
        file.write(f"DEPLOY_PATH = {Config.get_instance().deploy_path_campaign}\n")
        file.write(f"OODLE_PATH = {Config.get_instance().oodle_path}\n")
        file.write(f"TAG_XML_TEMPLATE_PATH = {Config.get_instance().tag_xml_template_path}\n")
     

