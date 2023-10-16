# import textwrap
# import config
#
# class Display:
#     def __init__(self, stdscr, curses):
#         self.stdscr = stdscr
#         self.curses = curses
#
#     def show_introduction(self, stdscr, introduction: str) -> int:
#         stdscr.clear()
#         intro_lines = textwrap.wrap(config.introduction, width)
#         start_row = 5
#         stdscr.attron(curses.color_pair(COLOR_TYPE))
#         for idx, item in enumerate(config.logos):
#             _x = max(width // 2 - len(item) // 2, 0)
#             _y = max(start_row - len(config.logos) // 2 + idx, 1)
#             stdscr.addstr(_y, _x, f"  {item}")
#         for i, line in enumerate(intro_lines):
#             _x = max(width // 2 - len(line) // 2, 0)
#             start_row = start_row + len(config.logos) // 2 + 2
#             stdscr.addstr(start_row, _x, line)
#         start_row += 1
#         _x = max(width // 2 - len(config.version) // 2, 0)
#         stdscr.refresh()
#         stdscr.addstr(start_row, _x, 'v-' + config.version)
#         stdscr.attroff(curses.color_pair(COLOR_TYPE))
#         stdscr.refresh()
#         return start_row
#
#     def say_goodbye(self, stdscr: dict):
#         stdscr.clear()
#         for i, line in enumerate(config.goodbyes):
#             x = max(width // 2 - len(line) // 2, 0)
#             y = max(height // 2 - len(config.goodbyes) // 2 + i, 0)
#             stdscr.addstr(y, x, f"  {line}", curses.color_pair(COLOR_TYPE))
#         stdscr.refresh()
#         time.sleep(config.goodbye_show_seconds)
