#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

int main () {
  int fd = open ("pic.ppm", O_WRONLY|O_CREAT);
  char firstlines[] = "P3 100 100 255";
  write (fd, firstlines, sizeof (firstlines));
  char rgb[3][3];
  int i,j;
  for (i = 0; i < 10; i++) {
    if (i < 3333) {
      itoa (255, rgb[0], sizeof (rgb[0]));
      itoa (random() %256, rgb[1], sizeof (rgb[1]));
      itoa (random() %256, rgb[2], sizeof (rgb[2]));
    }
    else if (i < 6666) {
      itoa (random() %256, rgb[0], sizeof (rgb[0]));
      itoa (255, rgb[1], sizeof (rgb[1]));
      itoa (random() %256, rgb[2], sizeof (rgb[2]));
    }
    else {
      itoa (random() %256, rgb[0], sizeof (rgb[0]));
      itoa (random() %256, rgb[1], sizeof (rgb[1]));
      itoa (255, rgb[2], sizeof (rgb[2]));
    }
    char color [12];
    strcpy (color, rgb[0]);
    strcat (color, rgb[1]);
    strcat (color, rgb[2]);
    write (fd, color, sizeof (color));
  }
  return 0;
}
