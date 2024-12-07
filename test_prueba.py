from problema_camino_mas_corto import camino_mas_corto


def test_prueba_tecnica():
    assert (
        camino_mas_corto(
        [   [0, 0, 0, 0], 
            [1, 1, 0, 1],
            [0, 0, 0, 0], 
            [0, 1, 1, 0]], 
            (0, 0), (3, 3)
        )
        == 6
    )


def test_sin_obstaculos():
    assert camino_mas_corto([[0, 0, 0], 
                             [0, 0, 0], 
                             [0, 0, 0]], (0, 0), (2, 2)) == 4


def test_inicio_destino_bloqueado():
    assert camino_mas_corto([[1, 0, 0], 
                             [0, 1, 0], 
                             [0, 0, 1]], (0, 0), (2, 2)) == -1
