package money

type Dollar struct {
	money
}

func (d *Dollar) Times(multiplier int) Money {
	return NewDollar(d.amount * multiplier)
}
func (d *Dollar) Equals(other any) bool {
	otherDollar, ok := other.(*Dollar)
	return ok && d.amount == otherDollar.amount
}
func (d *Dollar) Currency() string {
	return "USD"
}
func NewDollar(amount int) *Dollar {
	return &Dollar{
		money: money{amount: amount},
	}
}
