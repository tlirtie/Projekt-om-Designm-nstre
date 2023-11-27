import tkinter as tk
import random

#Alle de forskellige matematiske operatorer er grupperet under en overordnet klasse, altså brug af Strategy-designmønstret.
class MatematikOperation:
    def execute(self, num1, num2):
        pass

#Dette er underklasserne med alle de specifikke matematiske operationer.
class Addition(MatematikOperation):
    def execute(self, num1, num2):
        return num1 + num2

class Subtraktion(MatematikOperation):
    def execute(self, num1, num2):
        return num1 - num2 if num1 >= num2 else num2 - num1

class Multiplikation(MatematikOperation):
    def execute(self, num1, num2):
        return num1 * num2

class Division(MatematikOperation):
    def execute(self, num1, num2):
        if num2 == 0 or num1 % num2 != 0 or num1 == num2 or num2 == 1:  #Dette gør så der ikke genereres division-spørgsmål hvor tallet divideres med sig selv eller divideres med 1, da disse spørgsmål vil være alt for lette.
            return "Udefineret"
        result = num1 // num2
        return result


class MatematikApp:
    #Dette loader appen og sætter titlen på programmet
    def __init__(self, root):
        self.root = root
        self.root.title("Matematikeren")
        self.current_question = None

        #Dette er teksten i programmet hvor skrifttype og størrelse er angivet.
        self.label = tk.Label(root, text="Vælg en opgavetype", font=("Helvetica", 16)) 
        self.label.pack()

        #Dette laver en dropdown-menu hvor brugeren kan vælge imellem de 4 forskellige matematiske operationer. Som standard har den addition med størrelse og skrifttype angivet.
        self.operation_var = tk.StringVar()
        self.operation_var.set("Addition")
        self.operation_menu = tk.OptionMenu(root, self.operation_var, "Addition", "Subtraktion", "Multiplikation", "Division")
        self.operation_menu.config(font=("Helvetica", 14)) 
        self.operation_menu.pack()

        #Her laves knappen som man kan klikke på for at generere et spørgsmål. Her vil den kalde kommandoen "generate_question" når den klikkes.
        self.generate_question_button = tk.Button(root, text="Generér spørgsmål", command=self.generate_question, font=("Helvetica", 14))  # Increase the font size
        self.generate_question_button.pack()

        #Her laves der et label, altså tekst, hvor det genererede spørgsmål indsættes
        self.question_label = tk.Label(root, text="", font=("Helvetica", 14)) 
        self.question_label.pack()

        #Her laves der et felt hvor brugeren kan inputte værdier.
        self.answer_entry = tk.Entry(root, font=("Helvetica", 14)) 
        self.answer_entry.pack()

        #Her laves der en knap som brugeren kan trykke på for at indsende sit svar. Herefter vil kommandoen "check_answer" kaldes hvorefter brugerens input sammenholdes med det rigtige svar. Igen er skrifttypen og størrelsen angivet, og teksten på knappen er "Indsend svar"
        self.submit_button = tk.Button(root, text="Indsend svar", command=self.check_answer, font=("Helvetica", 14))  #Skrifttype og størrelse for "Indsend svar"-knap
        self.submit_button.pack()

    #Her genereres spørgsmålene.
    def generate_question(self):
        selected_operation = self.operation_var.get()

        #Hvis der er valgt en addition-opgave, vil der blive genereret et tal indenfor intervallet [1:50] i både num1 og num2
        if selected_operation == "Addition":
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            self.question_label.config(text=f"Hvad er {num1} + {num2} ?")

        #Hvis der er valgt en subtraktion-opgave, vil der tages et tilfældigt tal fra intervallet [1:50] i num1 og [1:num1] i num2. Dette er for at tallene ikke ender ud med at blive negative tal, da vores målgruppe jo er de mindre klassetrin i folkeskolen, så spørgsmålene må ikke blive for svære. Derfor bliver num2 aldrig højere end num1.
        elif selected_operation == "Subtraktion":
            num1 = random.randint(1, 50)
            num2 = random.randint(1, num1)
            self.question_label.config(text=f"Hvad er {num1} - {num2} ?")

        #Hvis der er valgt en multiplikation-opgave, vil der blive genereret et tilfældigt tal i intervallet[1:10] i både num1 og num2. Dette er for at opgaverne ikke ender ud med at være alt for svære, hvilket er hvad der ville ske hvis vi ganger svære tocifrede tal.
        elif selected_operation == "Multiplikation":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            self.question_label.config(text=f"Hvad er {num1} * {num2} ?")

        #Dette er division. Her genereres der et tal i num1 og num2 indenfor intervallet [2:20].
        else:
            num1 = random.randint(2, 20) 
            num2 = random.randint(2, 20)

            while num2 == num1 or num2 == 1 or num2 == 0 or num1 % num2 != 0: #Her sørges der for at num1 ikke er num2, da dette vil være et alt for nemt spørgsmål. Derudover sørges der for at num2 ikke er enten 1 eller 0, da dette også vil være for nemt. Så sørges der til sidst også for at divisionen mellem num1 og num2 ender med et helt tal og ikke et kommatal, og det er for at det ikke bliver for avanceret for vores målgruppe, hvilket jo er elever i de mindre klassetrin.
                num1 = random.randint(2, 20)
                num2 = random.randint(2, 20)

            self.question_label.config(text=f"Hvad er {num1} / {num2} ?")

        #Her opbevares info vedrørende spørgsmålet i baggrunden af programmet. Når spørgsmålet er svaret på, slettes det, og der genereres et nyt inden for den valgte matematiske operator.
        for operation in [Addition(), Subtraktion(), Multiplikation(), Division]:
            if operation.__class__.__name__ == selected_operation:
                self.current_question = (num1, num2, operation)
                self.answer_entry.delete(0, tk.END)
                self.submit_button.config(state=tk.NORMAL)

    #Denne del sammenholder brugerens input med det rigtige svar.
    def check_answer(self):
        if self.current_question is None:
            return

        num1, num2, operation = self.current_question
        user_answer = self.answer_entry.get()

        try:
            user_answer = int(user_answer)
            correct_answer = operation.execute(num1, num2)

            if user_answer == correct_answer:
                self.generate_question()
            else:
                self.question_label.config(text=f"Forkert! Det rigtige svar var {correct_answer}")
                self.answer_entry.delete(0, tk.END)
        except ValueError: #Hvis et tal ikke indtastes, eller hvis der indtastes bogstaver i stedet for tal, så udskriv det nedenstående.
            self.question_label.config(text="Indtast venligst et gyldigt tal")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatematikApp(root)
    
    #Størrelse af vindue. Bredde gange højde
    root.geometry("400x250")

    root.mainloop()


