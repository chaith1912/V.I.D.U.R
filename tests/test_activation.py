from app.core.activation import ActivationSystem


def main():

    activation = ActivationSystem()

    activated = activation.wait_for_activation()

    print()

    if activated:
        print("✓ V.I.D.U.R. ACTIVATION SUCCESSFUL")
    else:
        print("✗ V.I.D.U.R. ACTIVATION FAILED")


if __name__ == "__main__":
    main()