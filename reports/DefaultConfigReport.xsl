<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" xmlns:math="http://exslt.org/math" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="DTD/xhtml1-strict.dtd" indent="yes" omit-xml-declaration="yes"/>
<xsl:template name="formatCost">
	<xsl:param name="cost"/>
	<xsl:variable name="plat" select="floor($cost div 10000000)"/>
	<xsl:variable name="gold" select="floor(($cost - $plat * 10000000) div 10000)"/>
	<xsl:variable name="silver" select="floor(($cost - $plat * 10000000 - $gold * 10000) div 100)"/>
	<xsl:variable name="copper" select="floor(($cost - $plat * 10000000 - $gold * 10000 - $silver * 100))"/>
	<xsl:if test="$plat &gt; 0"><xsl:copy-of select="$plat"/>p<xsl:text> </xsl:text></xsl:if>
	<xsl:if test="$gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$gold"/>g<xsl:text> </xsl:text></xsl:if>
	<xsl:if test="$silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$silver"/>s<xsl:text> </xsl:text></xsl:if>
	<xsl:if test="$copper &gt; 0 or $silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$copper"/>c</xsl:if>
</xsl:template>

<xsl:template name="lineBreak">
<xsl:text>
</xsl:text>
</xsl:template>

<xsl:template match="/SCTemplate">
<body>
<center><b>Config Report</b></center><br />
<center><b>Stats</b></center><hr />
<table cellspacing="10" cellpadding="0">
<xsl:call-template name="lineBreak"/>
<xsl:for-each select="Stats/*">
	<xsl:if test="name() != 'AF' and name() != 'PowerPool'">
	<xsl:if test="position() mod 3 = 1"><xsl:text disable-output-escaping="yes">&lt;tr&gt;</xsl:text></xsl:if>
	<td><xsl:value-of select="substring(name(),1,3)"/>:</td>
	<td><xsl:value-of select="TotalBonus"/> / </td>
	<td><xsl:value-of select="BaseCap"/></td>
	<xsl:if test="position() mod 3 = 0 or position() = (last() - 2)"><xsl:text disable-output-escaping="yes">&lt;/tr&gt;
	</xsl:text></xsl:if>
	</xsl:if>
</xsl:for-each>
</table><br />
<center><b>Resists</b></center><hr />
<table cellspacing="10" cellpadding="0">
<xsl:for-each select="Resists/*">
	<xsl:if test="position() mod 3 = 1"><xsl:text disable-output-escaping="yes">&lt;tr&gt;</xsl:text></xsl:if>
	<td><xsl:value-of select="name()"/>:</td>
	<td><xsl:value-of select="TotalBonus"/><xsl:for-each select="RacialBonus"> (+<xsl:value-of select="."/>)</xsl:for-each> / </td>
	<td><xsl:value-of select="BaseCap"/></td>
	<xsl:if test="position() mod 3 = 0 or position() = last()"><xsl:text disable-output-escaping="yes">&lt;/tr&gt;</xsl:text></xsl:if>
</xsl:for-each>
<xsl:call-template name="lineBreak"/>
</table><br />
<xsl:call-template name="lineBreak"/>
<xsl:for-each select="Skills|Focus|OtherBonuses|PvEBonuses">
	<xsl:if test="math:max(./*/TotalBonus) &gt; 0">
		<center><b><xsl:value-of select="name()"/></b></center><hr />
		<table>
		<xsl:for-each select="./*">
			<xsl:if test="substring(name(),1,3) != 'All'">
				<xsl:call-template name="lineBreak"/>
				<tr><td align="right"><xsl:value-of select="TotalBonus"/> / </td>
				<td><xsl:value-of select="BaseCap"/></td>
				<td><xsl:value-of select="name()"/></td></tr>
			</xsl:if>
		</xsl:for-each>
		<xsl:call-template name="lineBreak"/>
		</table>
	</xsl:if>
</xsl:for-each>
<xsl:call-template name="lineBreak"/>
<center><b>Piece Listing</b></center><hr />
<xsl:for-each select="SCItem">
	<xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
		<dl>
		<dt><b><xsl:value-of select="Location" /></b></dt>
		<dd>
		<!--<tr><td colspan="4" align="center"><b><xsl:value-of select="Location" /></b></td></tr> -->
		<table>
		<tr><td colspan="5">Name: <xsl:value-of select="Name"/></td></tr>
		<tr><td colspan="5">Level: <xsl:value-of select="Level"/>
		Quality: <xsl:value-of select="ItemQuality"/>
		AF/DPS: <xsl:value-of select="AFDPS"/>
		Bonus: <xsl:value-of select="Bonus"/></td></tr>
		<xsl:if test="ActiveState = 'drop'">
			<tr><td colspan="5">Imbue Points: <xsl:value-of select="Imbue"/>
			&#160;&#160;&#160;of <xsl:value-of select="ItemImbue"/>
			&#160;&#160;&#160;Quality: <xsl:value-of select="ItemQuality"/>
			&#160;&#160;&#160;Overcharge: <xsl:value-of select="Overcharge"/></td></tr>
		</xsl:if>
		<xsl:for-each select="SLOT">
			<xsl:variable name="slotnum">
				<xsl:value-of select="number(@Number) + 1"/>
			</xsl:variable>
			<xsl:if test="Type != 'Unused'">
				<xsl:choose>
					<xsl:when test="number(@Number) &lt;= 4 and ../ActiveState = 'player'">
						<tr><td>Gem <xsl:copy-of select="$slotnum"/>:</td>
						<td align="right"><xsl:value-of select="Amount"/></td>
						<td><xsl:value-of select="Effect"/></td>
						<td> - <xsl:value-of select="Qua"/></td>
						<td><xsl:value-of select="Name"/></td></tr>
					</xsl:when>
					<xsl:otherwise>
						<tr><td>Effect <xsl:copy-of select="$slotnum"/>:</td>
						<td align="right"><xsl:value-of select="Amount"/></td>
						<td><xsl:value-of select="Effect"/></td>
						<td>
						<xsl:if test="../ActiveState = 'player'">
							 - <xsl:value-of select="Name"/>
						</xsl:if>
						</td></tr>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
		</xsl:for-each>
		<tr><td colspan="5">Utility: <xsl:value-of select="Utility"/></td></tr>
		<xsl:if test="ActiveState = 'player'">
			<tr><td colspan="5">Cost: 
				<xsl:call-template name="formatCost">
					<xsl:with-param name="cost" select="Cost"/>
				</xsl:call-template>
			&#160;&#160;&#160;Price: 
				<xsl:call-template name="formatCost">
					<xsl:with-param name="cost" select="Price"/>
				</xsl:call-template>
			</td></tr>
		</xsl:if>
		<tr><td colspan="5">&#160;</td></tr>
		</table>
		</dd>
		</dl>
	</xsl:if>
</xsl:for-each>
</body>
</xsl:template>
</xsl:stylesheet>
