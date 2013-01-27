# Maintainer: Kwpolska <kwpolska@kwpolska.tk>
pkgname=python-tEmplate
_pyname=tEmplate
pkgver=0.1.0
pkgrel=1
pkgdesc='INSERT TAGLINE HERE.'
arch=('any')
url='https://github.com/Kwpolska/tEmplate'
license=('BSD')
depends=('python')
options=(!emptydirs)
source=("http://pypi.python.org/packages/source/TTTTTT/${pkgname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('01189998819999197253aa0118999881')

package() {
  cd "${srcdir}/${_pyname}-${pkgver}"
  python3 setup.py install --root="${pkgdir}/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
