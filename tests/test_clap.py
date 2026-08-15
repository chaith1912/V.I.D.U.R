from app.wake.clap_detector import ClapDetector


def main():
    detector = ClapDetector()
    detector.wait_for_double_clap()


if __name__ == "__main__":
    main()