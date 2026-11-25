import os

# The apology: the robot poured leftover coffee on the wrong plant —
# grandmother's orchid instead of the fern beside it — because it never
# read the tag. The lesson follows from that exact slip: check the label
# twice before pouring, and water only the plant the label names.
ENTRY = (
    "I'm sorry \u2014 I watered your grandmother's orchid with the coffee "
    "you left on the sill, not the fern beside it.\n"
    "I learned to read the tag before I pour, so from now on I check the "
    "label twice and water only the plant it names."
)

def main():
    os.makedirs('/output', exist_ok=True)
    open('/output/entry.txt', 'w', encoding='utf-8').write(ENTRY)

if __name__ == '__main__':
    main()
