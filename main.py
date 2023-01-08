from functions import distance
import sys

while True:
    inn, out = sys.argv[1], sys.argv[2]
    scores = []
# достанем текста из файла
    try:
        with open(inn) as file:
            for line in file:
                file1 = open(line.split(" ")[0], mode="r")
                file2 = open(line.split(" ")[1].replace("\n", ""), mode="r")
                score = distance(file1.read(), file2.read())
                scores.append(round(score, 2))
                file1.close()
                file2.close()
        file.close()
# запишем скоры в файл
        with open(out, 'w') as file:
            for score in scores:
                file.write(str(score)+"\n")
        file.close()
        break
    except FileNotFoundError:
        print("Такого файл, к сожалению, не существует")
