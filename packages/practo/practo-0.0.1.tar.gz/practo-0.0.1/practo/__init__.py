class BankersAlgorithm:
    def __init__(self, allocation, max_resources, available_resources):
        self.allocation = allocation  # Allocation matrix (process x resource)
        self.max_resources = max_resources  # Max resources needed matrix (process x resource)
        self.available_resources = available_resources  # Available resources vector (resource)
        self.num_processes = len(allocation)
        self.num_resources = len(available_resources)

    def is_safe_state(self):
        # Initialize work and finish vectors
        work = self.available_resources.copy()
        finish = [False] * self.num_processes

        # Initialize a sequence to store safe sequence
        safe_sequence = []

        # Loop through all processes
        for _ in range(self.num_processes):
            # Find a process that can be executed
            for process in range(self.num_processes):
                if not finish[process]:
                    # Check if resources are available for this process
                    if all(work[i] >= self.max_resources[process][i] - self.allocation[process][i] for i in range(self.num_resources)):
                        # Add the process to the safe sequence
                        safe_sequence.append(process)
                        # Release allocated resources
                        work = [work[i] + self.allocation[process][i] for i in range(self.num_resources)]
                        finish[process] = True
                        break

        # If all processes are in the safe sequence, return True
        if all(finish):
            print("Safe Sequence:", safe_sequence)
            return True
        else:
            print("Unsafe State")
            return False
        

class bully:
    def __init__(self,st,prio,co,n):
        self.st=st
        self.prio=prio
        self.co=co
        self.n=n
    
    # iterating till the range
    def getval(self):
        for i in range(0, self.n):
            print("Enter Status of the system",i+1,":")
            self.st.append(int(input()))
            print("Enter Priority of the system")
            self.prio.append(int(input())) 
        

    def elect(self,ele):
        ele=ele-1
        self.co=ele+1
        for i in range(0, self.n):
            if(self.prio[ele]<self.prio[i]):
                print("Election message is sent from ",(ele+1)," to ",(i+1),)
                if(self.st[i]==1):
                    self.elect(i+1)
        return self.co

    def startelect(self):
        ele=int(input("Which process will initiate election?"))
        print("Final coordinator is ",self.elect(ele))


