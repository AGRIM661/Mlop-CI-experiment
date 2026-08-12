from model import train_model


def test_model_accuracy():
    accuracy = train_model()

    assert 0 <= accuracy <= 1