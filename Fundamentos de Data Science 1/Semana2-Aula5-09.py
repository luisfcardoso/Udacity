
#Python 3

def create_cast_list(filename):
    cast_list = []
    # usar with para abrir o arquivo filename
    with open(filename) as f:
    	# use a sintaxe do laço for para processar cada linha
    	# e adicione o nome do ator a cast_list
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    	return cast_list

print(create_cast_list('flying_circus_cast.txt'))