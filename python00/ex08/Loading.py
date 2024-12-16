def ft_tqdm(lst: range):
    """
        Custom progress bar replicating tqdm() function
    """
    total = len(lst)
    for i, item in enumerate(lst, 1):
        progress = i / total
        filled_bar = int(100 * progress)
        bar = "=" * filled_bar + ">" + " " * (100 - filled_bar)
        percentage = int(progress * 100)
        print(f"\r{percentage}%|[{bar}]| {i}/{total}", end="", flush=True)
        yield item


def main():
    for elem in ft_tqdm(range(333)):
        pass
    print()


if __name__ == "__main__":
    main()
