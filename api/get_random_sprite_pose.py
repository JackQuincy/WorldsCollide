
def get_random_sprite_pose():
  import rng as random
  from graphics.sprites.sprites import id_sprite
  from graphics.palettes.palettes import id_palette

  from seed import generate_seed
  seed = generate_seed()
  random.seed(seed)

  CHARACTER_POSES = [1, 9, 10, 11, 16, 20, 22, 24, 29, 31, 32, 36]
  
  sprite = random.choice(list(id_sprite.keys()))
  palette = random.choice(list(id_palette.keys()))
  pose = random.choice(CHARACTER_POSES)
  
  return (int(sprite), int(palette), int(pose))