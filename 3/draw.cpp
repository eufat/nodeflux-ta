/*
This answer rather long. The alternative is by parsing an grayscale image to create desired output.
*/

#include <stdio.h>
#include <iostream>

int draw_dot(int j, int bound_1, int bound_2, int bound_3, int bound_4) {
      char a = '*';
      if (j > bound_1 && j < bound_4)
            a = ' ';
      if (j > bound_2 && j < bound_3)
            a = '*';
      std::cout << a;
}

int main()
{
      const int row = 12;
      const int col = 32;
      const int mid = 16;

      for (int i = 0; i < row; i++)
      {
            for (int j = col; j > 0; j--)
            {
                  switch(i) {
                        case 0:
                              draw_dot(j, 0, 0, 0, 0);
                              break;
                        case 1:
                              draw_dot(j, 14, 16, 16, 19);
                              break;
                        case 2:
                              draw_dot(j, 9, 16, 16, 24);
                              break;
                        case 3:
                              draw_dot(j, 7, 12, 21, 26);
                              break;
                        case 10:
                              draw_dot(j, 7, 10, 23, 26);
                              break;
                        case 11:
                              draw_dot(j, 0, 0, 0, 0);
                              break;
                        default:
                              draw_dot(j, 6, 11, 22, 27);
                              break;
                  }
            }
            std::cout << std::endl;
      }
}

