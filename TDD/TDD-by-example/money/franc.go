package money

type Franc struct {
	money
}

func (f *Franc) Times(multiplier int) Money {
	return NewFranc(f.amount * multiplier)
}
func (f *Franc) Equals(other any) bool {
	otherFranc, ok := other.(*Franc)
	return ok && f.amount == otherFranc.amount
}
func (f *Franc) Currency() string {
	return "CHF"
}
func NewFranc(amount int) *Franc {
	return &Franc{
		money: money{amount},
	}
}
