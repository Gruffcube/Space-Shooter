_entity_counters = {}


class Entity:
    def __init__(self, gameloop):
        # Init variables
        self.x = 0
        self.y = 0

        self.destroyed = False
        self.hidden = False

        self.routines = []

        # Assign unique id
        self.entity_name = str(type(self).__name__)
        if self.entity_name in _entity_counters.keys():
            _entity_counters[self.entity_name] += 1
            numeric_id = _entity_counters[self.entity_name]
        else:
            _entity_counters[self.entity_name] = 0
            numeric_id = 0
        self.id = f"{type(self).__name__}<{numeric_id}>"

        # Add self to parent gameloop
        self.gameloop = gameloop
        self.gameloop.entities.append(self)
        self.gameloop.entity_registry[self.id] = self

        print(f"Created entity {self.id}")

    def start_routine(self, gen):
        self.routines.append({"gen": gen, "timer": 0})

    def update(self):
        if self.destroyed:
            return
        
        self._pre_routine()
        self._run_routines()
        self._post_routine()

    def destroy(self):
        self.destroyed = True
        self.routines.clear()
        print(f"Destroyed entity {self.id}")

    def render(self):
        if not self.hidden:
            vis_x = self.x - self.gameloop.cam_x
            vis_y = self.y - self.gameloop.cam_y
            self._draw(vis_x, vis_y)
        else:
            pass

    def _draw(self, vis_x, vis_y):
        raise NotImplementedError(
            "ERROR: Entity <{self.entity_name}> does not have a _draw function. All visible entities must have one!"
        )

    def _pre_routine(self):
        pass

    def _run_routines(self):
        surviving_routines = []

        for routine in self.routines:
            if routine["timer"] > 0:
                routine["timer"] -= self.gameloop.dt

                surviving_routines.append(routine)

            else:
                try:
                    next_delay = next(routine["gen"])
                    routine["timer"] = next_delay - self.gameloop.dt

                    surviving_routines.append(routine)

                except StopIteration:
                    pass

        self.routines = surviving_routines

    def _post_routine(self):
        pass
