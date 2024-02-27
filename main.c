#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
enum {
    BLACK,
    DARK_BLUE,
    DARK_GREEN,
    DARK_SKYBLUE,
    DARK_RED,
    DARK_VIOLET,
    DAKR_YELLOW,
    GRAY,
    DARK_GRAY,
    BLUE,
    GREEN,
    SKYBLUE,
    RED,
    VIOLET,
    YELLOW,
    WHITE,
};
char oksync = NULL;
char clear_sync() {
    oksync = NULL;
    return oksync;
}
int main() {
    SetConsoleTitle(TEXT("H.O.S_NNDB.2311 v1.3.1"));
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BLUE);
    printf("The current version of the program is 1.2.1, which is a version written as Python 3.12 based on C\n");
    printf("The current version of the program may be unstable\nAre you sure you want to get started?[Y/N]: ");
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), WHITE);
    while (1) {
        oksync = NULL;
        scanf_s("%s", &oksync,sizeof(1));
        if (oksync == 'Y') {
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), RED);
            printf("Can end Window now");
            system("Start.py");
            break;
        }
        if (oksync == 'N') {
            printf("Exit the program\nUse the Data Archive site to use a different version");
            Sleep(3000);
            exit(0);
        }
        else {
            printf("Please enter Y or N\n");
            clear_sync(oksync);
            continue;
        }
        return 0;
    }
}