package money

type Expression interface {
	Reduce(bank *Bank, to string) Money
	Plus(amount Expression) Expression
}

type Sum struct {
	Augend Expression
	Addend Expression
}

func (s *Sum) Reduce(bank *Bank, to string) Money {
	amount := s.Augend.Reduce(bank, to).getAmount() +
		s.Addend.Reduce(bank, to).getAmount()
	return newMoney(amount, to)
}
func (s *Sum) Plus(amount Expression) Expression {
	// TODO: implement this
	return nil
}

func NewSum(augend, addend Expression) *Sum {
	return &Sum{
		Augend: augend,
		Addend: addend,
	}
}
