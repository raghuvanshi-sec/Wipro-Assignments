def sort_colors(colors):
    color_list = colors.split("-")
    color_list.sort()
    return "-".join(color_list)

colors = input("Enter hyphen-separated colors: ")

print("Sorted colors:", sort_colors(colors))