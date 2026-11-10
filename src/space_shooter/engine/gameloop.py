import pygame
import copy


class GameLoop:
    def __init__(self, screen, asset_manager):
        self.asset_manager = asset_manager
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.entity_registry = {}
        self.entities = []
        
        self.screen_width, self.screen_height = self.screen.get_size()
        
        self.cam_x = 0
        self.cam_y = 0
        
        self.pressed_keys = pygame.key.get_pressed()
        
        self.tick_counter = 0
        
        
    def run(self):
        self.running = True
        while self.running:
            self.pressed_keys = pygame.key.get_pressed()
            
            self.dt = self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
            
            self._engine_update()
            self._update()
            
            self._engine_render()
            
            self.tick_counter += 1
            
        return
    
    def stop(self):
        self.running = False
    
    def get_entity(self, entity_id):
        return self.entity_registry.get(entity_id)
    
    def _update(self):
        pass
    
    def _engine_update(self):
        for entity in self.entities:
            entity.update()
        
        # Prune destroyed entities
        i = 0
        while i < len(self.entities):
            if self.entities[i].destroyed:
                del self.entity_registry[self.entities[i].id]
                del self.entities[i]
                
            else:
                i += 1
        
    def _engine_render(self):
        self.screen.fill((30, 30, 30))
        for entity in self.entities:
            entity.render()
        pygame.display.flip()
