#!/usr/bin/env python
import angr

def main():
  PROGRAM = "./simple"
  GOOD_PATH = 0x4005a8
  BAD_PATH = 0x4005b4
  CHAR_RANGE = (0x20, 0x7e)
  input_size = 0x1

  project = angr.Project(PROGRAM)
  argv1 = angr.claripy.BVS("argv1", input_size * 8)

  initial_state = project.factory.entry_state(args=[PROGRAM, argv1]) 
  initial_state.add_constraints(argv1.chop(8)[0] > CHAR_RANGE[0])
  initial_state.add_constraints(argv1.chop(8)[0] < CHAR_RANGE[1])
  initial_path = project.factory.path(initial_state)
  path_group = project.factory.path_group(initial_state)
  path_group.explore(find=GOOD_PATH, avoid=BAD_PATH)

  found = path_group.found[0]
  solution = found.state.se.any_str(argv1)

  return solution

def test():
  assert main() == 'a'

if __name__ == '__main__':
  print(repr(main()))
