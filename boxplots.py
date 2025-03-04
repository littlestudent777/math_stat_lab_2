import os
import matplotlib.pyplot as plt
import seaborn as sns


def build_boxplots(sample_size: list[int], distributions: list) -> None:

    save_path = "boxplots"
    os.makedirs(save_path, exist_ok=True)  # Create a directory for graphs, if it doesn't exist

    for distribution_name, distribution_f in distributions:
        figure, axes = plt.subplots(3, 1, figsize=(20, 10))
        figure.suptitle(f'{distribution_name} distribution', fontsize=18)

        for index, n in enumerate(sample_size):
            values = distribution_f(n)

            sns.boxplot(values, ax=axes[index], orient='h', color='skyblue',
                        medianprops=dict(color='salmon'), whiskerprops=dict(color='purple'),
                        flierprops=dict(marker='o', markersize=5, markerfacecolor='green'))

            # Special handling for Cauchy because it has a big tail
            if distribution_name == "Cauchy" and n > 50:
                    axes[index].set_xscale('symlog')  # symlog to display negative values
                    axes[index].set_xlabel('symlog of x')
            else:
                axes[index].set_xlabel('x')

            axes[index].set_title(f'n = {n}')

        plt.subplots_adjust(hspace=0.5)
        figure.savefig(os.path.join(save_path, f"{distribution_name}.png"), dpi=300)
