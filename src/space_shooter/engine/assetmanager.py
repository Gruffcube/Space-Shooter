from pathlib import Path 
import os
import pygame


class AssetManager:
    def __init__(self):
        self._image_cache = {}
        self._sound_cache = {}
        self._font_cache = {}
        
        self.base_path = Path(__file__).resolve().parents[1] / "assets"
        
        os.makedirs(self.base_path / "images", exist_ok=True)
        os.makedirs(self.base_path / "sounds", exist_ok=True)
        os.makedirs(self.base_path / "fonts", exist_ok=True)
                
    
    def load_image(self, filename, convert_alpha=True):
        if filename in self._image_cache:
            return self._image_cache[filename]
        
        full_path = self.base_path / "images" / filename
        
        try:
            image = pygame.image.load(full_path)
            
            if convert_alpha:
                image = image.convert_alpha()
            else:
                image = image.convert()
                
            self._image_cache[filename] = image 
            
            return image
        
        except pygame.error as e:
            print(f"Failed to load image [{full_path}]. e: [{e}]")


    def load_sound(self, filename):
        if filename in self._sound_cache:
            return self._sound_cache[filename]
        
        full_path = self.base_path / "sounds" / filename
        
        try:
            sound = pygame.mixer.Sound(full_path)
            self._sound_cache[filename] = sound 
            
            return sound
        
        except pygame.error as e:
            print(f"Failed to load sound [{full_path}]. e: [{e}]")
           
            
    def load_font(self, filename, size):
        key = (filename, size)
        if key in self._font_cache:
            return self._font_cache[key]
        
        full_path = self.base_path / "fonts" / filename
        
        try:
            font = pygame.font.Font(full_path, size)
            self._font_cache[key] = font 
            
            return font
        
        except pygame.error as e:
            print(f"Failed to load font [{key}]. e: [{e}]")
    
    def wipe_cache(self):
        self._image_cache = {}
        self._sound_cache = {}
        self._font_cache = {}
    
    def unload_image(self, filename):
        del self._image_cache[filename]
        
    def unload_sound(self, filename):
        del self._sound_cache[filename]

    def unload_font(self, filename, size):
        del self._sound_cache[(filename, size)]
