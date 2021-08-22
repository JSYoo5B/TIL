#include <cstdio>

int main(void) {
	int month, day;
	int day_of_the_week;

	scanf("%d %d", &month, &day);
	// for calculating nth day of the month, decrease month by 1
	while (month--) {
		switch(month) {
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				day += 31;
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				day += 30;
				break;
			case 2:
				day += 28;
				break;
			default:
				break;
		}

	}

	day_of_the_week = day % 7;
	switch(day_of_the_week) {
		case 0:
			printf("SUN");
			break;
		case 1:
			printf("MON");
			break;
		case 2:
			printf("TUE");
			break;
		case 3:
			printf("WED");
			break;
		case 4:
			printf("THU");
			break;
		case 5:
			printf("FRI");
			break;
		case 6:
			printf("SAT");
			break;
		default:
			break;
	}
}