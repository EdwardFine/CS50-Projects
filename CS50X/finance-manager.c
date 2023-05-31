#include <stdio.h>
#include <cs50.h>

#define MAX_EXPENSES 100

typedef struct{
    char* name;
    double amount;
}Expense;

void addExpense(Expense expenses[], int *numExpenses){
    if(*numExpenses >= MAX_EXPENSES){
        printf("Max expenses reached.");
        return;
    }

    Expense newExpense;

    newExpense.name = get_string("Expense name: ");
    newExpense.amount = get_double("Expense amount: ");

    expenses[*numExpenses] = newExpense;
    (*numExpenses)++;
    return;
}

void printExpenses(Expense expenses[], int numExpenses){
    printf("Expense List:\n");
    for(int i = 0; i < numExpenses; i++){
        printf("%s, costs $%.2lf\n",expenses[i].name,expenses[i].amount);
    }
    return;
}

double calculateTotalExpenses(Expense expenses[], int numExpenses){
    double sum = 0;
    for(int i = 0; i < numExpenses; i++){
        sum += expenses[i].amount;
    }
    return sum;
}

int main(){
    Expense expenses[MAX_EXPENSES];
    int numExpenses = 0;
    int choice;

    do{
        printf("\nPersonal Finance Manager\n");
        printf("1. Add an expense\n");
        printf("2. Print all expenses\n");
        printf("3. Calculate total expense\n");
        printf("4. Exit\n");
        choice = get_int("Enter your choice: ");
        printf("\n");

        switch(choice){
            case 1:
                addExpense(expenses,&numExpenses);
                break;
            case 2:
                printExpenses(expenses, numExpenses);
                break;
            case 3:
                printf("Total Expenses: $%.2lf\n",calculateTotalExpenses(expenses, numExpenses));
                break;
            case 4:
                printf("Exiting Program");
                break;
            default:
                printf("Invalid Input");
                break;
        }
    }while(choice != 4);
    return 0;
}
