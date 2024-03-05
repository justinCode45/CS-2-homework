class Decimal
{
public:
    long long int p;
    long long int q;
    Decimal(long long int p, long long int q);
    Decimal operator+(const Decimal &d);
    Decimal operator-(const Decimal &d);
    Decimal operator*(const Decimal &d);
    Decimal operator/(const Decimal &d);
    Decimal operator-();
    void simplify();
}

Decimal::Decimal(long long int p, long long int q)
{
    this->p = p;
    this->q = q;
}

Decimal Decimal::operator+(const Decimal &d)
{
    return Decimal(this->p * d.q + d.p * this->q, this->q * d.q);
}

Decimal Decimal::operator-(const Decimal &d)
{
    return Decimal(this->p * d.q - d.p * this->q, this->q * d.q);
}

Decimal Decimal::operator*(const Decimal &d)
{
    return Decimal(this->p * d.p, this->q * d.q);
}

Decimal Decimal::operator/(const Decimal &d)
{
    return Decimal(this->p * d.q, this->q * d.p);
}

Decimal Decimal::operator-()
{
    return Decimal(-this->p, this->q);
}

void Decimal::simplify()
{
    long long int a = this->p;
    long long int b = this->q;
    while (b != 0)
    {
        long long int r = a % b;
        a = b;
        b = r;
    }
    this->p /= a;
    this->q /= a;
}

