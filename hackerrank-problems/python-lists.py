if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command_ = input().split()
        # print(command_)
        
        if command_[0] == "insert":
            l.insert(int(command_[1]), int(command_[2]))
        
        elif command_[0] == "print":
            print(l)
            
        elif command_[0] == "remove":
            l.remove(int(command_[1]))
        
        elif command_[0] == "append":
            l.append(int(command_[1]))
        
        elif command_[0] == "pop":
            l.pop()
            
        elif command_[0] == "reverse":
            l = l[::-1]
        
        
        elif command_[0] == "sort":
            l.sort()
            
    
