#include "brforsegment.h"

BrForSegment::BrForSegment(int x1, int y1, int x2, int y2, QWidget *parent ): QWidget(parent)
{
    const int deltaX = abs(x2 - x1);
    const int deltaY = abs(y2 - y1);
    const int signX = x1 < x2 ? 1 : -1;
    const int signY = y1 < y2 ? 1 : -1;
    int error = deltaX - deltaY;
    QPointF p;
    p.setX(x2);
    p.setY(y2);
    points.push_back(p);
    while(x1 != x2 || y1 != y2)
   {
        p.setX(x1);
        p.setY(y1);
        points.push_back(p);
        int error2 = error * 2;
        if(error2 > -deltaY)
        {
            error -= deltaY;
            x1 += signX;
        }
        if(error2 < deltaX)
        {
            error += deltaX;
            y1 += signY;
        }
    }
}
