
from chess.chess import Chess, chesses
from chess.tempPoint.tempPoint import createTempPoint
from chess.tot.tot import createTot
from chess.king.king import createKing
from chess.si.si import createSi
from chess.xe.xe import createXe
from chess.phao.phao import createPhao
from chess.ma.ma import createMa
from chess.tuong.tuong import createTuong

def setChess():
        createTempPoint()
        createTot()
        createKing()
        createSi()
        createXe()
        createPhao()
        createMa()
        createTuong()
        
