import json
from app.models.student import Estudiante, EstudianteEncoder


def test_estudiante_encoder():
    # Create an instance of Estudiante
    estudiante = Estudiante(
        cedula='0106207038',
        primer_apellido='Carrion',
        segundo_apellido='Cuenca',
        primer_nombre='Marlon',
        segundo_nombre='Anibal'
    )

    # Use the custom JSON encoder to convert the Estudiante instance to JSON
    estudiante_json = json.dumps(estudiante, cls=EstudianteEncoder)

    # Expected JSON representation of the Estudiante instance
    expected_json = '{"cedula": "0106207038", "primer_apellido": "Carrion", "segundo_apellido": "Cuenca", ' \
                    '"primer_nombre": "Marlon", "segundo_nombre": "Anibal"}'

    # Check if the JSON representation is as expected
    assert estudiante_json == expected_json
