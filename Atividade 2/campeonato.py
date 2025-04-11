{
    "test_cases": [
        {
            "participante": {
                "idade": 9,
                "categoria": "infantil",
                "tempoEstimado": 45,
                "assinaturaTermo": true
            },
            "expected": false
        },
        {
            "participante": {
                "idade": 16,
                "categoria": "infantil",
                "tempoEstimado": 45,
                "assinaturaTermo": true
            },
            "expected": false
        },
        {
            "participante": {
                "idade": 20,
                "categoria": "adulto",
                "tempoEstimado": 25,
                "assinaturaTermo": true
            },
            "expected": false
        },
        {
            "participante": {
                "idade": 18,
                "categoria": "adulto",
                "tempoEstimado": 45,
                "assinaturaTermo": false
            },
            "expected": false
        },
        {
            "participante": {
                "idade": 15,
                "categoria": "juvenil",
                "tempoEstimado": 45,
                "assinaturaTermo": true
            },
            "expected": true
        },
        {
            "participante": {
                "idade": 10,
                "categoria": "infantil",
                "tempoEstimado": 30,
                "assinaturaTermo": true
            },
            "expected": true
        },
        {
            "participante": {
                "idade": 60,
                "categoria": "adulto",
                "tempoEstimado": 180,
                "assinaturaTermo": true
            },
            "expected": true
        }
    ]
}